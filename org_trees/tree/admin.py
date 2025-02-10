from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')  
    list_filter = ('parent',)  
    search_fields = ('name',)  
    ordering = ('id',)  

admin.site.register(Employee, EmployeeAdmin)
