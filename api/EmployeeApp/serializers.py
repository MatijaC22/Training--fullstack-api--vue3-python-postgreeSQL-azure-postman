#help to convert complex types or model instances into native python data types that can then easily rendered into json or xml or other content types
#they also help in deserialization which is nothing but converting the past data back to complex types

from rest_framework import serializers
from EmployeeApp.models import Departments,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentID','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeID','EmployeeName','Department','DateOfJoining','PhotoFileName')

    