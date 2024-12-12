from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Student
from .forms import StudentForm

def demopage(request):
    return HttpResponse('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRQLqpG5HYINEUP7UYV6ZtUcVTA-vTmeE1mQ&s" style="height: 100%;widt: 100%;"/> ')
def homepage(request):
    return render(request, 'home.html')    
def aboutus(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')     
def myform(request):
    return render(request, 'form.html')
def formprocess(request):
    a = int(request.POST["txt1"])
    b = int(request.POST["txt2"])
    c = a + b
    return render(request, "ans.html",{'mya':a,'myb':b,'myc':c})

def addStudent(request):
    if request.method == 'GET':
        context = {'form':StudentForm()}
        return render(request,'add.html',context)
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(addStudent)
        else:
            return render(request, 'add.html', {'form': form})
