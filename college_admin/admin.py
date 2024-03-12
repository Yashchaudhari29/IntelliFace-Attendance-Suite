from django.contrib import admin
from college_admin.models import *


class regAdmin(admin.ModelAdmin):
    list_display =  ('en_no','name','img')

admin.site.register(register,regAdmin)