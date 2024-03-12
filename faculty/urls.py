
from django.urls import path
from faculty.views import *
urlpatterns = [
    path('',F_home,name='F_home'),
    path('export-to-excel/', download_excel_data, name='export_to_excel'),
    path('empty/', empty_db, name='empty'),
]
