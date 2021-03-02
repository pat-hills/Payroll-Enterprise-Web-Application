from django.contrib.auth.backends import ModelBackend
from appusers.models import User


class EmailAuthBackend(ModelBackend):
    """
    Email Authentication Backend

    Allows a user to sign in using an email/password pair, then check
    a username/password pair if email failed
    """

    def authenticate(self, email=None, password=None):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
                return None

    






    
