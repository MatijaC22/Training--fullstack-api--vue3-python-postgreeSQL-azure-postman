#What is views? In the Django framework, views are Python functions or classes that receive a web request and return a web response. The response can be a simple HTTP response, an HTML template response, or an HTTP redirect response that redirects a user to another page.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # to be able to allo other domains to acces our api methods
from rest_framework.parsers import JSONParser # to parse(devide) incoming data into data model
from  django.http.response import JsonResponse
#When a page is requested, Django creates an HttpRequest object that contains metadata about the request. Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. Each view is responsible for returning an HttpResponse object.

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer


from django.core.files.storage import default_storage #default storage module to save the file

# Create your views here.


#What is API?
#logic which is used as intermiddiater so two aplications can comunicate
#API is the acronym for Application Programming Interface, which is a software 
#intermediary that allows two applications to talk to each other. Each time you
#use an app like Facebook, send an instant message, or check the weather on your 
#phone, you're using an API.

@csrf_exempt # decorator ( @ ) is used to add another function (csrf_exempt) in this function
def departmentApi(request,id=0): #the method will recieve an optional id which we will need to use in the delete method
    if request.method == 'GET': # in get method we will return all the records in json format
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments,many=True) #we are making use of serializer class to convert it into json format
        return JsonResponse(departments_serializer.data,safe=False) #the parameter safe=false is basivally used to inform django that while we are trying to convert to json is actuallty valid format and we are fine is there are still any issue in it
    elif request.method =='POST': #used to insert new records into departments table
        department_data = JSONParser().parse(request) #parsing request
        departments_serializer = DepartmentSerializer(data=department_data) #using serializer to convert it inot model
        if departments_serializer.is_valid(): #if model valid, save in database
            departments_serializer.save()
            return JsonResponse("Added Sucessfully", safe=False) #and return success message
        return JsonResponse("Failed to Add", safe=False)
    elif request.method =='PUT': #used to update a given record
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentID=department_data['DepartmentID']) #first we are capturing the existing record using department id
        departments_serializer = DepartmentSerializer(department,data=department_data) #maping with new value using serializer class
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Sucessfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentID=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt # decorator ( @ ) is used to add another function (csrf_exempt) in this function
def employeeApi(request,id=0): #the method will recieve an optional id which we will need to use in the delete method
    if request.method == 'GET': # in get method we will return all the records in json format
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees,many=True) #we are making use of serializer class to convert it into json format
        return JsonResponse(employees_serializer.data,safe=False) #the parameter safe=false is basivally used to inform django that while we are trying to convert to json is actuallty valid format and we are fine is there are still any issue in it
    elif request.method =='POST': #used to insert new records into employees table
        employee_data = JSONParser().parse(request) #parsing request
        employees_serializer = EmployeeSerializer(data=employee_data) #using serializer to convert it inot model
        if employees_serializer.is_valid(): #if model valid, save in database
            employees_serializer.save()
            return JsonResponse("Added Sucessfully", safe=False) #and return success message
        return JsonResponse("Failed to Add", safe=False)
    elif request.method =='PUT': #used to update a given record
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeID=employee_data['EmployeeID']) #first we are capturing the existing record using employee id
        employees_serializer = EmployeeSerializer(employee,data=employee_data) #maping with new value using serializer class
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Sucessfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeID=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)