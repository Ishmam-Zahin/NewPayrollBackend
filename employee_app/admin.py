from django.contrib import admin
from .models import GlobalComponent, GlobalComponentConditions, Employee, CustomComponent

# Register your models here.
admin.site.register(GlobalComponent)
admin.site.register(GlobalComponentConditions)
admin.site.register(Employee)
admin.site.register(CustomComponent)
