from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from appusers.models import User
from employee.models import *
from organization.models import *
from organization.services import *
from .models import *
from .services import *
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from django.contrib import messages
from employee.services import *

# Create your views here.





@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def all_employee_payroll_data(request):
    employee__payroll_records = get_all_employee_payroll()
    #user_organization_allowance = get_user_organzation_allowances_set_up_configurations(user_organization)
    #user_organization_deduction = get_user_organization_deductions_set_up_configurations(user_organization) 
    context = {'employee__payroll_records' : employee__payroll_records}
    return render(request, 'payroll/all_payroll.html',context)




@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def all_employee_allowance_data(request):


    if request.method == "POST":
        allowance = request.POST['allowance']
        employee = request.POST['employee']

        allowance_post_data = get_organization_allowance_by_id(allowance)

        employee_data = get_employee_record_by_id(employee)
 


        if verify_allowance.exists():
            messages.add_message(request, messages.WARNING, 'Allowance Already Added For The month!.')
            return HttpResponseRedirect(reverse("payroll:all_employee_allowance_data"))



        


        save_employee_allowance = Allowanceroll.objects.create(employee_allowance=employee_data.employee_job_details,allowance_given_by=request.user,allowance_type=allowance_post_data)

        if save_employee_allowance:
            messages.add_message(request, messages.SUCCESS, 'Successfully recorded employee allowance!.')
            return HttpResponseRedirect(reverse("payroll:all_employee_allowance_data"))




      #id =  request.POST["id"]
#         delete_employee_job_details_a = delete_employee_job_details(id)

#         if delete_employee_job_details_a:
#             delete_employee(id)

#             messages.add_message(request, messages.WARNING, 'Successfully deleted employee record!.')
#             return HttpResponseRedirect(reverse("employee:all_employee"))

 
    else:


        all_employees = get_all_employee_records()
        employee_allowance_records = get_all_employee_allowance()
        compliance_allowance = organzation_allowances_set_up_configurations()
    #user_organization_allowance = get_user_organzation_allowances_set_up_configurations(user_organization)
    #user_organization_deduction = get_user_organization_deductions_set_up_configurations(user_organization) 
        context = {'employee_allowance_records' : employee_allowance_records,'all_employees' : all_employees,'compliance_allowance' : compliance_allowance}
        return render(request, 'payroll/all_allowance.html',context)





# @login_required(login_url="appusers:login_user")
# @cache_control(no_cache=True, must_revalidate=True,no_store=True)
# def prepare_employee_payroll(request,id):

#     if request.method == "POST":


#         id =  request.POST["id"]
#         delete_employee_job_details_a = delete_employee_job_details(id)

#         if delete_employee_job_details_a:
#             delete_employee(id)

#             messages.add_message(request, messages.WARNING, 'Successfully deleted employee record!.')
#             return HttpResponseRedirect(reverse("employee:all_employee"))

 
#     else:

#         return render(request, 'employees/all_employee_list.html')





@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def record_payroll_for_employee(request):

        verify_payroll = validate_payroll_for_the_month_and_year()


        if verify_payroll.exists():
            messages.add_message(request, messages.WARNING, 'Payroll Already Run For The month!.')
            return HttpResponseRedirect(reverse("payroll:all_employee_payroll_data"))

        records_  = get_all_employee_records()

        if records_employees:
            for pay_roll_data in records_employees: 
                Payroll.objects.create(amount_paid=pay_roll_data.salary,employee_payroll=pay_roll_data.employee_job_details,payroll_paid_by=request.user)
            messages.add_message(request, messages.SUCCESS, 'Successfully run employee payroll for the month!.')
            return HttpResponseRedirect(reverse("payroll:all_employee_payroll_data"))



   
        return render(request, 'payroll/all_payroll.html')






@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def employee_pay_slip(request,employee_id,pay_id):

    employee_single_record = get_employee_record_by_id(employee_id)
    emplo_yee = employee_single_record.employee_job_details
    employee_pay_roll_record = get_payroll_record_by_id(pay_id)

    employee_payr_roll_date_for_allowance = employee_pay_roll_record.date_created.month
 

    allowances_sum = get_sum_of_all_employee_allowance_by_date(emplo_yee,employee_payr_roll_date_for_allowance)

    deductions_percentage_sum = get_sum_all_organization_deductions_percentage()

    deductions_monetary_sum = get_sum_all_organization_deductions_monetary()

    #employee_gross_salary = float(allowances_sum) + float(employee_pay_roll_record.amount_paid)

    employee_salary = employee_pay_roll_record.amount_paid
 

    organization_details = get_user_organization(request)


    context = {'employee_single_record' : employee_single_record,'employee_pay_roll_record' : employee_pay_roll_record,
    'employee_allowance_records_by_payroll_date':employee_allowance_records_by_payroll_date,'organization_deductions':organization_deductions,'employee_salary':employee_salary,
    'allowances_sum':allowances_sum,'deductions_percentage_sum':deductions_percentage_sum,'deductions_monetary_sum':deductions_monetary_sum,'organization_details':organization_details,}
    #employee__payroll_records = get_all_employee_payroll()
    #user_organization_allowance = get_user_organzation_allowances_set_up_configurations(user_organization)
    #user_organization_deduction = get_user_organization_deductions_set_up_configurations(user_organization) 
    #context = {'employee__payroll_records' : employee__payroll_records}
    return render(request, 'payroll/view_salary_slip.html',context)





