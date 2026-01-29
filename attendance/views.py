from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from .models import Attendance
from .serializers import AttendanceSerializer
from employees.models import Employee

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['employee__full_name', 'employee__employee_id']
    ordering_fields = ['date', 'created_at']
    ordering = ['-date']
    
    def get_queryset(self):
        """Filter attendance by employee if specified"""
        queryset = Attendance.objects.all()
        employee_id = self.request.query_params.get('employee_id', None)
        
        if employee_id:
            queryset = queryset.filter(employee_id=employee_id)
        
        return queryset
    
    def create(self, request, *args, **kwargs):
        """Mark attendance for an employee"""
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'])
    def employee_records(self, request):
        """Get attendance records for a specific employee"""
        employee_id = request.query_params.get('employee_id', None)
        
        if not employee_id:
            return Response(
                {'error': 'employee_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return Response(
                {'error': f'Employee with ID {employee_id} not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        records = Attendance.objects.filter(employee=employee).order_by('-date')
        serializer = self.get_serializer(records, many=True)
        
        # Calculate statistics
        total_records = records.count()
        total_present = records.filter(status='PRESENT').count()
        total_absent = records.filter(status='ABSENT').count()
        
        return Response({
            'employee': {
                'id': employee.id,
                'name': employee.full_name,
                'employee_id': employee.employee_id,
                'email': employee.email,
            },
            'records': serializer.data,
            'stats': {
                'total': total_records,
                'present': total_present,
                'absent': total_absent,
            }
        })
    
    @action(detail=False, methods=['get'])
    def filter_by_date(self, request):
        """Filter attendance records by date range"""
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        
        queryset = Attendance.objects.all()
        
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        """Get attendance summary for all employees"""
        employees = Employee.objects.all()
        summary = []
        
        for employee in employees:
            records = Attendance.objects.filter(employee=employee)
            total_present = records.filter(status='PRESENT').count()
            
            summary.append({
                'employee_id': employee.id,
                'name': employee.full_name,
                'total_present': total_present,
                'total_absent': records.filter(status='ABSENT').count(),
                'total_records': records.count(),
            })
        
        return Response(summary)

