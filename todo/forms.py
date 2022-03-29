from django import forms

class AgregarTarea(forms.form):
   tarea = forms.CharField()
from django import forms

class AgregarTarea(forms.Form):
	tarea = forms.CharField()