from .models import *
from hr360.utils import *



def get_user_by_email(email):
    user_email = User.objects.get(is_deleted=False,email=email)
    return user_email