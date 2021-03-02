from django.urls import path

from . import views

app_name = "employee"
urlpatterns = [
    path("organization/view/records/employees", views.all_employee, name="all_employee"), 
    path("organization/add/records/employee", views.create_employees, name="create_employees"),
    path("organization/view/record/employee/<int:id>", views.view_employee_record, name="view_employee_record"),
    path("organization/delete/record/employee/<int:id>", views.delete_employee_record, name="delete_employee_record"), 
    path("organization/edit/record/employee/<int:id>", views.edit_employee_record, name="edit_employee_record"), 
      
]