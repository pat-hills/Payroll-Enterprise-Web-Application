from organization.models import *



def get_user_organization(request):
    try:
        user_organization = Organization.objects.get(is_deleted=False,user_organization=request.user)
        return user_organization
    except Organization.DoesNotExist:
        return None



def get_user_organzation_allowances_set_up_configurations(organization):
    try:
        user_allowances_setup = ComplianceAllowance.objects.filter(is_deleted=False,user_organization_compliance_allowance =organization)
        return user_allowances_setup
    except ComplianceAllowance.DoesNotExist:
        return None


def get_user_organization_deductions_set_up (organization):
    try:
        user_deduction_setup = ComplianceDeduction.objects.filter(is_deleted=False,user_organization_compliance_deduction=organization)
        return user_deduction_setup
    except ComplianceDeduction.DoesNotExist:
        return None



 

def organzation_allowances_set_up_configurations():
    try:
        user_allowances_setup = ComplianceAllowance.objects.filter(is_deleted=False)
        return user_allowances_setup
    except ComplianceAllowance.DoesNotExist:
        return None



def get_organization_allowance_by_id(id):
    try:
        allowance = ComplianceAllowance.objects.get(is_deleted=False,pk=id)
        #return get_summary_submitted_monthly_report_by_id
    except ComplianceAllowance.DoesNotExist:
        allowance = None
    
    return allowance






def update_user_organization_details(id,name,tagline,physical_address,location,postal_address,primary_contact,email,webiste,summary_of_services,logo): 
    update_organization_details_query = Organization.objects.filter(is_deleted=False,id=id).update(name=name,tagline=tagline,addresss=physical_address,location=location,postal_address=postal_address,
    primary_contact=primary_contact,email=email,webiste=webiste,summary_of_services=summary_of_services,logo=logo)
    return update_organization_details_query


