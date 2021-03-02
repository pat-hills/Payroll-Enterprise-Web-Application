

from employee.models import *

from .models import *
import datetime
from django.db.models import Sum


def get_all_employee_payroll():
    try:
        employee_all_payroll = Payroll.objects.filter(is_deleted=False).prefetch_related("employee_payroll","payroll_paid_by")
        return employee_all_payroll
    except Payroll.DoesNotExist:
        return None



def validate_payroll_for_the_month_and_year():
    try:
        today = datetime.datetime.now()
        current_year = today.year
        current_month = today.month

        verify_month = Payroll.objects.filter(is_deleted=False,date_created__year = current_year,date_created__month = current_month)
        return verify_month

    except Payroll.DoesNotExist:
        return None




def get_all_employee_allowance():
    try:
        employee_all_allowance = Allowanceroll.objects.filter(is_deleted=False).prefetch_related("employee_allowance","allowance_given_by","allowance_type")
        #employee_all_allowance = Allowanceroll.objects.filter(is_deleted=False)
        return employee_all_allowance
    except Allowanceroll.DoesNotExist:
        return None


 



def get_payroll_record_by_id(id):
    try:
        employee_pay_roll = Payroll.objects.prefetch_related("employee_payroll","payroll_paid_by").get(is_deleted=False,pk=id)
        #return get_summary_submitted_monthly_report_by_id
    except Payroll.DoesNotExist:
        employee_pay_roll = None
    
    return employee_pay_roll


def get_all_employee_allowance_by_date(employee,date_month):
    try:
        employee_all_allowance_date_record = Allowanceroll.objects.filter(is_deleted=False,employee_allowance=employee,date_created__month=date_month).prefetch_related("employee_allowance","allowance_given_by","allowance_type")
        #employee_all_allowance = Allowanceroll.objects.filter(is_deleted=False)
        return employee_all_allowance_date_record
    except Allowanceroll.DoesNotExist:
        return None



def get_sum_of_all_employee_allowance_by_date(employee,date_month):
    try:
        employee_all_allowance_sum = Allowanceroll.objects.filter(is_deleted=False,employee_allowance=employee,date_created__month=date_month).aggregate(allowances_sum=Sum("allowance_type__amount"))
        
        return employee_all_allowance_sum
    except Allowanceroll.DoesNotExist:
        return None


def get_all_organization_deductions():
    try:
        employee_all_deductions = ComplianceDeduction.objects.filter(is_deleted=False)
        #employee_all_allowance = Allowanceroll.objects.filter(is_deleted=False)
        return employee_all_deductions
    except ComplianceDeduction.DoesNotExist:
        return None


def get_sum_all_organization_deductions_monetary():
    try:
        #Percentage(%)
        employee_all_deductions_monetary_sum = ComplianceDeduction.objects.filter(is_deleted=False,unit_of_category="Monetary").aggregate(deductions_monetary_sum=Sum("unit_of_value"))
        #employee_all_deductions_monetary_sum = ComplianceDeduction.objects.filter(is_deleted=False,unit_of_category="Monetary").aggregate(Sum("unit_of_value"))['unit_of_value__sum']
        #employee_all_allowance = Allowanceroll.objects.filter(is_deleted=False)
        return employee_all_deductions_monetary_sum
    except ComplianceDeduction.DoesNotExist:
        return None




def get_sum_all_organization_deductions_percentage():
    try:

        #employee_all_deductions_percentage_sum = ComplianceDeduction.objects.filter(is_deleted=False,unit_of_category="Percentage(%)").aggregate(Sum("unit_of_value"))['unit_of_value__sum']/100
        #Percentage(%)
        employee_all_deductions_percentage_sum = ComplianceDeduction.objects.filter(is_deleted=False,unit_of_category="Percentage(%)").aggregate(deductions_percentage_sum=Sum("unit_of_value")/100)
        #employee_all_allowance = Allowanceroll.objects.filter(is_deleted=False)
        return employee_all_deductions_percentage_sum
    except ComplianceDeduction.DoesNotExist:
        return None

