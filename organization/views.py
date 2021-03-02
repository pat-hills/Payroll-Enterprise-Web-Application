from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from appusers.models import User
from .models import *
from .services import *
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from django.contrib import messages

# Create your views here.



# @login_required(login_url="appusers:login_user")
# @cache_control(no_cache=True, must_revalidate=True,no_store=True)
# def organization_setting(request): 
#     return render(request, 'organization/organization_setting.html')


@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def organization_setting(request):
    user_organization = get_user_organization(request)
    user_organization_allowance = get_user_organzation_allowances_set_up_configurations(user_organization)
    user_organization_deduction = get_user_organization_deductions_set_up_configurations(user_organization) 
    context = {'user_organization_allowance' : user_organization_allowance,'user_organization_deduction' : user_organization_deduction, 'user_organization':user_organization}
    return render(request, 'organization/organization_setting.html',context)



@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def create_organization_allowances(request):
    if request.method == "POST":
        
        allowance_name = request.POST["allowance_name"]
        allowance_amount = request.POST["allowance_amount"]

        user_organization = get_user_organization(request)

        

        save_organization_allowance = ComplianceAllowance.objects.create(name=allowance_name,amount=allowance_amount,
        user_compliance_allowance=request.user,user_organization_compliance_allowance=user_organization)
        save_organization_allowance.save()

       
        
        #return reverse('institution:institution',args=(request.session["institution_name"]))
        messages.add_message(request, messages.SUCCESS, 'Successfully created allowance!.')
        return HttpResponseRedirect(reverse("organization:organization_setting"))
    else:
         #user_customer_metrics = get_user_institution_custom_metrics(request)
         return render(request, "organization/organization_setting.html",{
     })






@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def create_organization_deduction(request):
    if request.method == "POST":
        
        deduction_name = request.POST["deduction_name"]
        deduction_unit_measurement = request.POST["deduction_unit_measurement"]
        
        deduction_value = float(request.POST["deduction_value"]) 

        if deduction_unit_measurement == "Percentage(%)" and deduction_value > 100:
            messages.add_message(request, messages.WARNING, 'Percentage values cannot be over 100%!.')
            return HttpResponseRedirect(reverse("organization:organization_setting"))


        user_organization = get_user_organization(request)

        

        save_organization_deductions = ComplianceDeduction.objects.create(name=deduction_name,unit_of_category=deduction_unit_measurement,unit_of_value=deduction_value,
        user_organization_compliance_deduction=user_organization,user_compliance_deduction=request.user)
        save_organization_deductions.save()

       
        
        #return reverse('institution:institution',args=(request.session["institution_name"]))
        messages.add_message(request, messages.SUCCESS, 'Successfully created deduction!.')
        return HttpResponseRedirect(reverse("organization:organization_setting"))
    else:
         #user_customer_metrics = get_user_institution_custom_metrics(request)
         return render(request, "organization/organization_setting.html",{
     })




@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def update_organization_details(request):
    if request.method == "POST":
        
        id = request.POST["id"]
        name = request.POST["name"]
        tagline = request.POST["tagline"]
        physical_address = request.POST["physical_address"]
        location = request.POST["location"]
        postal_address = request.POST["postal_address"]
        primary_contact = request.POST["primary_contact"]

        
        email = request.POST["email"]
        website = request.POST["website"]

        summary_of_services = request.POST["summary_of_services"]
        logo = request.FILES["logo"]

        user_organization = get_user_organization(request)

        

        save_organization_update = update_user_organization_details(id,name,tagline,physical_address,location,postal_address,primary_contact,email,website,summary_of_services,logo)
        if save_organization_update:
            OrganizationUploads.objects.create(logo=logo,user_organization_upload=request.user,organization_upload=user_organization)
            messages.add_message(request, messages.SUCCESS, 'Successfully updated organization details!.')
            return HttpResponseRedirect(reverse("organization:organization_setting"))


       
        
        #return reverse('institution:institution',args=(request.session["institution_name"]))
        #messages.add_message(request, messages.SUCCESS, 'Successfully created deduction!.')
        #return HttpResponseRedirect(reverse("organization:organization_setting"))
    else:
         #user_customer_metrics = get_user_institution_custom_metrics(request)
         return render(request, "organization/organization_setting.html",{
     })


