from django.contrib import admin
from .models import Employee, Sport


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    pass


class SportAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Sport, SportAdmin)

admin.site.site_header = 'Haritha Computers & Technology'
