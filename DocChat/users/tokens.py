from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six  


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """
    Custom token generator class for account activation in Django.

    This class inherits from PasswordResetTokenGenerator to generate tokens for account activation.

    Methods:
    - _make_hash_value(user, timestamp): Generates a hash value using user's primary key, timestamp, and user's active status.

    Attributes:
    - account_activation_token: Instance of AccountActivationTokenGenerator used for token generation.
    """
    def _make_hash_value(self, user, timestamp):
        """
        Generates a hash value using user's primary key, timestamp, and user's active status.

        Args:
        - user: User object.
        - timestamp: Timestamp value.

        Returns:
        - str: Concatenation of user's primary key, timestamp, and user's active status as a string.
        """
        return (
            six.text_type(user.pk) + six.text_type(timestamp)  + six.text_type(user.is_active)
        )


# Instance of AccountActivationTokenGenerator used for token generation.
account_activation_token = AccountActivationTokenGenerator()