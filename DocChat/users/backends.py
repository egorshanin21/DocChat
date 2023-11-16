from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()


class EmailBackend(ModelBackend):
    """
    Authenticates users based on their email or username.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticate a user based on the provided username or email along with the password.

        Args:
            request: The HTTP request object
            username: The username or email to be used for authentication
            password: The password for the user

        Returns:
            The authenticated user instance if successful, otherwise returns None.
        """
        try:
            # Check if a user with the provided username or email exists
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            # If the user does not exist, return None (no user found)
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            # If multiple users found, retrieve the first one based on ID ordering
            user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()
        # Check if the password matches and the user is allowed to authenticate
        if user.check_password(password) and self.user_can_authenticate(user):
            return user