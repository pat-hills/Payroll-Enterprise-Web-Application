from django.db import models
from appusers.models import User
from organization.models import *
from employee.models import *

# Create your models here.


class Payroll(models.Model):
    amount_paid = models.FloatField(null=False)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateField(null=False, auto_now=True)
    date_time_created = models.DateTimeField(null=False, auto_now=True)
    employee_payroll = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False,related_name="employee_payroll")
    payroll_paid_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False,related_name="payroll_paid_by") 

    def __str__(self):
         return "%s %s" % (self.id)




class Loanroll(models.Model):
    amount_loan = models.FloatField(null=False)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateField(null=False, auto_now=True)
    date_time_created = models.DateTimeField(null=False, auto_now=True)
    employee_loan_roll = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False,related_name="employee_loan_roll")
    given_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False,related_name="given_by") 
    comments = models.TextField(null=True)
    terms = models.CharField(max_length=128, null=True) 
    paid_status = models.CharField(max_length=128, null=False,default='PENDING') 
    user_paid_to = models.ForeignKey(User, on_delete=models.CASCADE, null=False,related_name="user_paid_to")


    def __str__(self):
         return "%s %s" % (self.id)





class Allowanceroll(models.Model):
    is_deleted = models.BooleanField(default=False) 
    date_created = models.DateField(null=False, auto_now=True)
    date_time_created = models.DateTimeField(null=False, auto_now=True)
    employee_allowance = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False,related_name="employee_allowance")  
    comments = models.TextField(null=True)
    allowance_given_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False,related_name="allowance_given_by")
    allowance_type = models.ForeignKey(ComplianceAllowance, on_delete=models.CASCADE, null=False,related_name="allowance_type")


    def __str__(self):
         return "%s %s" % (self.id)



 


