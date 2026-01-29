from django.core.management.base import BaseCommand
from employees.models import Employee
from attendance.models import Attendance
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seed database with sample employees and attendance records'

    def handle(self, *args, **options):
        # Check if data already exists
        if Employee.objects.exists():
            self.stdout.write(self.style.WARNING('Database already has employees. Skipping seed.'))
            return

        # Create sample employees
        employees_data = [
            {
                'employee_id': 'EMP001',
                'full_name': 'Alice Johnson',
                'email': 'alice.johnson@example.com',
                'department': 'IT'
            },
            {
                'employee_id': 'EMP002',
                'full_name': 'Bob Smith',
                'email': 'bob.smith@example.com',
                'department': 'HR'
            },
            {
                'employee_id': 'EMP003',
                'full_name': 'Carol White',
                'email': 'carol.white@example.com',
                'department': 'SALES'
            },
            {
                'employee_id': 'EMP004',
                'full_name': 'David Brown',
                'email': 'david.brown@example.com',
                'department': 'FINANCE'
            },
            {
                'employee_id': 'EMP005',
                'full_name': 'Emma Davis',
                'email': 'emma.davis@example.com',
                'department': 'MARKETING'
            },
        ]

        employees = []
        for emp_data in employees_data:
            emp = Employee.objects.create(**emp_data)
            employees.append(emp)
            self.stdout.write(self.style.SUCCESS(f'Created employee: {emp.full_name}'))

        # Create sample attendance records for the last 10 days
        base_date = datetime.now().date()
        statuses = ['PRESENT', 'ABSENT', 'PRESENT', 'PRESENT', 'PRESENT', 'PRESENT', 'PRESENT', 'ABSENT', 'PRESENT', 'PRESENT']

        for employee in employees:
            for i in range(10):
                attendance_date = base_date - timedelta(days=i)
                status = statuses[i % len(statuses)]
                
                Attendance.objects.create(
                    employee=employee,
                    date=attendance_date,
                    status=status
                )

        self.stdout.write(self.style.SUCCESS('✓ Successfully seeded database with sample data!'))
