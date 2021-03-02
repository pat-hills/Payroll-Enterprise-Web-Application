from django.urls import path
from . import views

app_name = "organization"
urlpatterns = [  
    path("organization/setting/setup/configuration", views.organization_setting, name="organization_setting"),
    path("organization/setting/setup/allowance", views.create_organization_allowances, name="create_organization_allowances"),
    path("organization/setting/setup/deduction", views.create_organization_deduction, name="create_organization_deduction"),
    path("organization/setting/setup/update_details", views.update_organization_details, name="update_organization_details"),
]

