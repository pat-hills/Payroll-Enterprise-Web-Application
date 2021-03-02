from django.db import models
from appusers.models import User

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=128,null=False)
    tagline = models.TextField(null=False, default='Tagline')
    addresss = models.CharField(max_length=128,null=False)
    location = models.CharField(max_length=128,null=False)
    postal_address = models.CharField(max_length=128,null=False)
    primary_contact = models.CharField(max_length=128, null=False)
    secondary_contact = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=128, null=False)
    webiste = models.CharField(max_length=128, null=False)
    summary_of_services = models.CharField(max_length=128, null=False)
    logo = models.ImageField(upload_to='businessLogo/', null=False)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateField(null=False, auto_now=True)
    date_time_created = models.DateTimeField(null=False, auto_now=True)
    user_organization = models.ForeignKey(User, on_delete=models.CASCADE, null=False,related_name="user_organization")

    def __str__(self):
         return "%s %s" % (self.name,self.tagline)




class ComplianceAllowance(models.Model):
    name = models.CharField(max_length=128,null=False)
    amount = models.FloatField(null=False)
    date_created = models.DateField(null=False, auto_now=True)
    date_time_created = models.DateTimeField(null=False, auto_now=True)
    is_deleted = models.BooleanField(default=False)
    user_organization_compliance_allowance = models.ForeignKey(Organization, on_delete=models.CASCADE, null=False,related_name="user_organization_compliance_allowance")
    user_compliance_allowance = models.ForeignKey(User, on_delete=models.CASCADE, null=False,related_name="user_compliance_allowance")

    def __str__(self):
         return "%s %s" % (self.name,self.amount)




class ComplianceDeduction(models.Model):
    name = models.CharField(max_length=128,null=False)
    unit_of_category = models.TextField(null=False)
    unit_of_value = models.FloatField(null=False)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateField(null=False, auto_now=True)
    date_time_created = models.DateTimeField(null=False, auto_now=True)
    user_compliance_deduction = models.ForeignKey(User, on_delete=models.CASCADE, null=False,related_name="user_compliance_deduction")
    user_organization_compliance_deduction = models.ForeignKey(Organization, on_delete=models.CASCADE, null=False,related_name="user_organization_compliance_deduction")

    def __str__(self):
         return "%s %s" % (self.name,self.unit_of_value)



class OrganizationUploads(models.Model):
    
    logo = models.FileField(upload_to='organizationUpload/', null=False)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateField(null=False, auto_now=True)
    date_time_created = models.DateTimeField(null=False, auto_now=True)
    user_organization_upload = models.ForeignKey(User, on_delete=models.CASCADE, null=False,related_name="user_organization_upload")
    organization_upload = models.ForeignKey(Organization, on_delete=models.CASCADE, null=False,related_name="organization_upload")

    def __str__(self):
         return "%s %s" % (self.id,self.logo)



 

