from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'parent', 'children']  # Ensure only hierarchical data is included

    def get_children(self, obj):
        children = Employee.objects.filter(parent=obj)
        return EmployeeSerializer(children, many=True).data  # Return only nested children
