from django import forms 
from .models import *
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=["name","roll","city","marks","passdate"]
class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=["name","empnum","city","salary","join_date"]

