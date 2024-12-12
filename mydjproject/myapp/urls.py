from django.urls import path 
from . import views

urlpatterns=[
    path("",views.demopage),
    path("home",views.homepage), 
    path("about",views.aboutus),
    path("contact",views.contact),
    path("contact/sam",views.contact),
    path("form",views.myform),
    path("process",views.formprocess),
    path("addstudent",views.addStudent),
    path("display",views.displayStudent),
]
