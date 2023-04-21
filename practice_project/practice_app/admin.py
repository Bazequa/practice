from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name","roll","city","marks","passdate"]
    def __str__(self):
        return self.name

@admin.register(Teacher)  
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name","empnum","city","salary","join_date"]
    def __str__(self):
        return self.name


 