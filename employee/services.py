from employee.models import *




def get_all_employee_records():
    try:
        employee_records = EmployeeJobDetails.objects.filter(is_deleted=False).prefetch_related("employee_job_details")
        return employee_records
    except EmployeeJobDetails.DoesNotExist:
        return None



# def get_employee_record_by_id(id):
#     try:
#         employee_records = EmployeeJobDetails.objects.get(is_deleted=False,id=id).prefetch_related("employee_job_details")
#         return employee_records
#     except EmployeeJobDetails.DoesNotExist:
#         return None



def get_employee_record_by_id(id):
    try:
        employee_records = EmployeeJobDetails.objects.select_related("employee_job_details").get(is_deleted=False,pk=id)
        #return get_summary_submitted_monthly_report_by_id
    except EmployeeJobDetails.DoesNotExist:
        employee_records = None
    
    return employee_records





def delete_employee_job_details(id): 
    delete_job_details = EmployeeJobDetails.objects.filter(id=id).update(is_deleted=True)
    return delete_job_details


def delete_employee(id): 
    delete_employee_record = Employee.objects.filter(id=id).update(is_deleted=True)
    return delete_employee_record




def edit_employee_records(id,first_name,last_name,residence,email,dob,home_town,place_of_birth,postal_address,primary_contact,secondary_contact,
    marital_status,social_security_number): 
    edit_record_employye = Employee.objects.filter(id=id).update(first_name=first_name,last_name=last_name,residence=residence,email=email,dob=dob,home_town=home_town,place_of_birth=place_of_birth,
    postal_address=postal_address,primary_contact=primary_contact,secondary_contact=secondary_contact,marital_status=marital_status,social_security_number=social_security_number)
    return edit_record_employye


def edit_employee_job_details_record(id,department,position_title,salary,bank,branch,acc_no,comments): 
    edit_job_details_record_employye = EmployeeJobDetails.objects.filter(id=id).update(department=department,position_title=position_title,salary=salary,acc_no=acc_no,comments=comments)
    return edit_job_details_record_employye


 
 

