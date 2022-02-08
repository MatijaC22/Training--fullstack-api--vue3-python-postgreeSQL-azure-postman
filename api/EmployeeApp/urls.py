from django.urls import re_path
from EmployeeApp import views

from django.conf.urls.static import static #adding url root for api method
from django.conf import settings


urlpatterns=[
    re_path(r'^department$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi), #Metacharacters are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:[] . ^ $ * + ? {} () \ | ----> https://www.programiz.com/python-programming/regex

    re_path(r'^employee$',views.employeeApi),
    re_path(r'^employee/([0-9]+)$',views.employeeApi), 

    re_path(r'^employee/savefile',views.SaveFile)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)