from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'employee_id', 'full_name', 'email', 'department', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_employee_id(self, value):
        """Ensure employee_id is unique and not empty"""
        if not value or not value.strip():
            raise serializers.ValidationError("Employee ID cannot be empty.")
        
        # Check for duplicates on create, and on update if value changed
        qs = Employee.objects.filter(employee_id=value)
        if self.instance is None:
            if qs.exists():
                raise serializers.ValidationError(f"Employee with ID '{value}' already exists.")
        else:
            # If updating and employee_id changed, ensure no other record uses it
            if value != self.instance.employee_id and qs.exists():
                raise serializers.ValidationError(f"Employee with ID '{value}' already exists.")
        
        return value
    
    def validate_email(self, value):
        """Ensure email is unique and properly formatted"""
        if not value or not value.strip():
            raise serializers.ValidationError("Email cannot be empty.")
        
        # Check for duplicates on create, and on update if value changed
        qs = Employee.objects.filter(email=value)
        if self.instance is None:
            if qs.exists():
                raise serializers.ValidationError(f"An employee with email '{value}' already exists.")
        else:
            if value != self.instance.email and qs.exists():
                raise serializers.ValidationError(f"An employee with email '{value}' already exists.")
        
        return value
    
    def validate_full_name(self, value):
        """Ensure full name is not empty"""
        if not value or not value.strip():
            raise serializers.ValidationError("Full name cannot be empty.")
        return value
