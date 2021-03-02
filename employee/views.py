from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from appusers.models import User
from organization.models import *
from organization.services import *
from .models import *
from .services import *
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from django.contrib import messages
import hashlib

# Create your views here.



@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def all_employee(request):
    employee_records = get_all_employee_records()
    #user_organization_allowance = get_user_organzation_allowances_set_up_configurations(user_organization)
    #user_organization_deduction = get_user_organization_deductions_set_up_configurations(user_organization) 
    context = {'employee_records' : employee_records}
    return render(request, 'employees/all_employee_list.html',context)





@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def create_employees(request):
    if request.method == "POST":
        
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        residence = request.POST["residence"]
        email = request.POST["email"]
        dob = request.POST["dob"]
        home_town = request.POST["home_town"]
        place_of_birth = request.POST["place_of_birth"]
        postal_address = request.POST["postal_address"]
        primary_contact = request.POST["primary_contact"]
        secondary_contact = request.POST["secondary_contact"]
        marital_status = request.POST["marital_status"]
        social_security_number = request.POST["social_security_number"]
        picture = request.FILES["picture"]

        department = request.POST["department"]
        position_title = request.POST["position_title"]
        salary = request.POST["salary"]
        bank = request.POST["bank"]
        branch = request.POST["branch"]
        acc_no = request.POST["acc_no"]
        comments = request.POST["comments"]


        mystring = email
        hash_obj = hashlib.md5(mystring.encode())
        code= hash_obj.hexdigest()


        

        

        save_organization_employee = Employee.objects.create(first_name=first_name,last_name=last_name,residence=residence,email=email,dob=dob,home_town=home_town,
        place_of_birth=place_of_birth,postal_address=postal_address,primary_contact=primary_contact,secondary_contact=secondary_contact,marital_status=marital_status,social_security_number=social_security_number,
        picture=picture,user_employee=request.user)
        save_organization_employee.save()
        if save_organization_employee:
            EmployeeJobDetails.objects.create(department=department,position_title=position_title,employee_code=code,salary=salary,bank=bank,branch=branch,acc_no=acc_no,comments=comments,employee_job_details=save_organization_employee,
            user_employee_job_details=request.user)

       
        
        #return reverse('institution:institution',args=(request.session["institution_name"]))
        messages.add_message(request, messages.SUCCESS, 'Successfully created employee!.')
        #return HttpResponseRedirect(reverse("employee:all_employee"))
        return HttpResponseRedirect(reverse("employee:view_employee_record",args=(save_organization_employee.id,)))
    else:
         #user_customer_metrics = get_user_institution_custom_metrics(request)
         return render(request, "employees/add_employee.html",{
     })




@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def view_employee_record(request,id):

        employee_single_record = get_employee_record_by_id(id)

        context = {'employee_single_record' : employee_single_record}


   
        return render(request, 'employees/view_employee_record.html',context)




@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def delete_employee_record(request,id):

    if request.method == "POST":


        id =  request.POST["id"]
        delete_employee_job_details_a = delete_employee_job_details(id)

        if delete_employee_job_details_a:
            delete_employee(id)

            messages.add_message(request, messages.WARNING, 'Successfully deleted employee record!.')
            return HttpResponseRedirect(reverse("employee:all_employee"))

 
    else:

        return render(request, 'employees/all_employee_list.html')




@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def edit_employee_record(request,id):

    if request.method == "POST":


        #id =  request.POST["id"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        residence = request.POST["residence"]
        email = request.POST["email"]
        dob = request.POST["dob"]
        home_town = request.POST["home_town"]
        place_of_birth = request.POST["place_of_birth"]
        postal_address = request.POST["postal_address"]
        primary_contact = request.POST["primary_contact"]
        secondary_contact = request.POST["secondary_contact"]
        marital_status = request.POST["marital_status"]
        social_security_number = request.POST["social_security_number"]
        #picture = request.FILES["picture"]

        department = request.POST["department"]
        position_title = request.POST["position_title"]
        salary = request.POST["salary"]
        bank = request.POST["bank"]
        branch = request.POST["branch"]
        acc_no = request.POST["acc_no"]
        comments = request.POST["comments"]


        edit_employee_records_data = edit_employee_records(id,first_name,last_name,residence,email,dob,home_town,place_of_birth,postal_address,primary_contact,
        secondary_contact,marital_status,social_security_number)

        if edit_employee_records_data:
            edit_employee_job_details_record(id,department,position_title,salary,bank,branch,acc_no,comments)

        #all_employee_data = get_employee_record_by_id(id)

        # if all_employee_data:
        #     all_employee_data.employee_job_details.first_name = first_name
        #     all_employee_data.employee_job_details.last_name = last_name
        #     all_employee_data.employee_job_details.residence = residence
        #     all_employee_data.employee_job_details.email = email
        #     all_employee_data.employee_job_details.dob = email
        #     all_employee_data.employee_job_details.home_town = home_town
        #     all_employee_data.employee_job_details.place_of_birth = place_of_birth
        #     all_employee_data.employee_job_details.postal_address = postal_address
        #     all_employee_data.employee_job_details.primary_contact = primary_contact
        #     all_employee_data.employee_job_details.secondary_contact = secondary_contact
        #     all_employee_data.employee_job_details.marital_status = marital_status
        #     all_employee_data.employee_job_details.social_security_number = social_security_number
        #     all_employee_data.employee_job_details.picture = picture

        #     all_employee_data.save()
            
            #edit_employee_job_details_record(id,department,position_title,salary,bank,branch,acc_no,comments)


            
            




            messages.add_message(request, messages.WARNING, 'Successfully edited employee record!.')
            return HttpResponseRedirect(reverse("employee:view_employee_record",args=(id,)))
            #return HttpResponseRedirect(reverse("employee:all_employee"))

 
    else:


        employee_single_record = get_employee_record_by_id(id)

        context = {'employee_single_record' : employee_single_record}



        return render(request, 'employees/edit_employee.html' ,context)