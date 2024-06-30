from django.contrib import admin

from .models import City, Country, Department, Employee, Project

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)
