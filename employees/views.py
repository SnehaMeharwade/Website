from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import get_object_or_404
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['full_name', 'employee_id', 'email']
    ordering_fields = ['created_at', 'full_name']
    ordering = ['-created_at']
    
    def create(self, request, *args, **kwargs):
        """Create a new employee with validation"""
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
    
    def destroy(self, request, *args, **kwargs):
        """Delete an employee"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': f'Employee {instance.full_name} deleted successfully.'},
            status=status.HTTP_200_OK
        )
    
    @action(detail=False, methods=['get'])
    def by_department(self, request):
        """Get employees filtered by department"""
        department = request.query_params.get('dept', None)
        if not department:
            return Response(
                {'error': 'Department parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        employees = Employee.objects.filter(department=department)
        serializer = self.get_serializer(employees, many=True)
        return Response(serializer.data)

