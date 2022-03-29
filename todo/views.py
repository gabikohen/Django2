from django.shortcuts import render
from django import forms

tareas = ['Django , Javascript , React , Hacking']
# Create your views here.

def home(request):
	context = {'tareas' : tareas}
	return render(request, "todo/home.html", context)



def add(request):
    form = AgregarTarea()
    context = {'form':form}
    return render(request,'todo/add.html',context)
