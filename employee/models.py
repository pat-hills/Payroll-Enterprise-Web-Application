from django.db import models
from appusers.models import User
from organization.models import *

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=128,null=False)
    last_name = models.CharField(max_length=128,null=False)
    residence = models.CharField(max_length=128,null=False)
    email = models.CharField(max_length=128, null=False)
    dob = models.DateField(null=False)
    home_town = models.CharField(max_length=128, null=False)
    place_of_birth = models.CharField(max_length=128,null=False)
    postal_address = models.CharField(max_length=128,null=False)
    primary_contact = models.CharField(max_length=128, null=False)
    secondary_contact = models.CharField(max_length=128, null=True)
    marital_status = models.CharField(max_length=128, null=False)
    social_security_number = models.CharField(max_length=128, null=False)
    picture = models.ImageField(upload_to='EmployeeUpload/', null=False)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateField(null=False, auto_now=True)
    date_time_created = models.DateTimeField(null=False, auto_now=True)
    user_employee = models.ForeignKey(User, on_delete=models.CASCADE, null=False,related_name="user_employee")
    employee_organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True,related_name="employee_organization")

    def __str__(self):
         return "%s %s" % (self.first_name,self.id)



class EmployeeJobDetails(models.Model):
    department = models.CharField(max_length=128,null=False)
    position_title = models.CharField(max_length=128,null=False)
    employee_code = models.CharField(max_length=128, null=True)
    start_date = models.DateField(null=True)
    salary = models.FloatField(null=False)
    bank = models.CharField(max_length=128,null=False)
    branch = models.CharField(max_length=128,null=False)
    acc_no = models.CharField(max_length=128,null=False)
    comments = models.TextField(null=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateField(null=False, auto_now=True)
    date_time_created = models.DateTimeField(null=False, auto_now=True)
    employee_job_details = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False,related_name="employee_job_details")
    user_employee_job_details = models.ForeignKey(User, on_delete=models.CASCADE, null=False,related_name="user_employee_job_details")
    employee_job_details_organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True,related_name="employee_job_details_organization")

    def __str__(self):
         return "%s %s" % (self.department,self.id)





