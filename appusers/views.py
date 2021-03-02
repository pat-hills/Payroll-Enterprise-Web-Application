from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from organization.models import Organization
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
#from .managers import UserAccount
from django.contrib import messages
from .utils import greetings 
#from repurta import securityuser
from hr360.securityuser import EmailAuthBackend

# Create your views here.


def index(request):
    return render(request, "account/login.html", {

    })


def register(request):

    if request.method == "POST":
        
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        confirmpassword = request.POST["confirmpassword"]
        account_type = "Business"
        user_role = "Administrator "
        is_institution_setup = False
        username = email+"_"+firstname+"_"+lastname

        # Ensure password matches confirmation
        if password != confirmpassword:
            return render(request, "account/register.html", {
                "message": "Passwords must match!"
            })


        user_email_qs = User.objects.filter(is_deleted=False, email=email).count()

        #user_email_qs = User.if_email_exist(email,email)

        if user_email_qs > 0 :

            return render(request, "account/register.html", {
               "message": "User account email already exist!"
           })
         
        
        #user_email_qs = UserAccount.objects.find_user_by_email(email)
        #if user_email_qs.exists():
            #return render(request, "account/institution_sign_up.html", {
               #"message": "User account email already exist!"
           # })

        
        user_save = User.objects.create_user(email=email,first_name = firstname,last_name = lastname,password=password,
        account_type = account_type,user_role = user_role,username=username)
        user_save.save()

        if user_save :
            organization_save_create = Organization.objects.create(user_organization = user_save)
            organization_save_create.save()
          
       

        #request.session["user_id"] = user_save.id
        request.session["fullname"] = user_save.first_name +" "+ user_save.last_name
        return HttpResponseRedirect(reverse('appusers:index'))
    else:
        return render(request, "account/register.html", {

    })




def login_user(request):

    if request.method == "POST":
        
        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]

        #user_auth = securityuser.EmailAuthBackend.authenticate(securityuser.EmailAuthBackend,email=email,password=password)
        user_auth = EmailAuthBackend.authenticate(EmailAuthBackend,email=email,password=password)

        # Check if authentication successful
        if user_auth is not None:
            login(request,user_auth)
            return HttpResponseRedirect(reverse("appusers:dashboard"))
        else:
            return render(request, "account/login.html", {
                "message": "Invalid username or password."
            })
    else:
        title = "Repurta - User Login"
        return render(request, "account/login.html", {
            "title" :  title

    })




@login_required(login_url="appusers:login_user")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def dashboard(request):
    #request.session['business_slug_name'] = business_name
    #we checking if user is valid to submit a report

    #user_business = get_user_business(request)

    #user_status_loan = get_user_business_active_institution_on_loan(request)
    #users_latest_loan_status = get_users_latest_loan_application(user_business)

    return render(request, "app/dashboard.html",{
         "greetings" : greetings,
     })




def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("appusers:index"))
