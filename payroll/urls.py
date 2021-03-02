from django.urls import path

from . import views

app_name = "payroll"
urlpatterns = [

      path("organization/view/records/payroll", views.all_employee_payroll_data, name="all_employee_payroll_data"),
      path("organization/view/records/payroll/pay", views.record_payroll_for_employee, name="record_payroll_for_employee"),
      path("organization/view/records/allowance", views.all_employee_allowance_data, name="all_employee_allowance_data"),
      path("organization/view/records/payslip/<int:employee_id>/<int:pay_id>", views.employee_pay_slip, name="employee_pay_slip"),
      #path("organization/view/record/employee/<int:id>", views.view_employee_record, name="view_employee_record"),
      # path("organization/view/record/employee/<int:id>", views.view_employee_record, name="view_employee_record"),       
      
]