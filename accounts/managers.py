from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _



class UserManager(BaseUserManager):
    """
    Custom user model manager where `email` is the unique identifiers
    for authentication instead of username.

    It also verifies the following mandatory fields where provided:
    -`first_name`
    -`last_name`
    -`residence_state`

    """

    def __create(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError(_('User must have Email Address'))
        if not extra_fields.get('first_name'):
            raise ValueError(_('User must have a First Name'))
        if not extra_fields.get('last_name'):
            raise ValueError(_('User must have a Last Name'))
        if not extra_fields.get('residence_state'):
            raise ValueError(_('User must have a state of residence'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        return user


    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email, password
        and the mandatory fields.
        
        """  
        ext_domain = email.split('@')

        if len(ext_domain) == 2 and ext_domain[1] == 'jijiremix.com':
            raise ValueError(_('Invalid email domain for user. domain cannot be @jijiremix.com'))

        user = self.__create(email=email, password=password, **extra_fields)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a StaffUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields['residence_state'] = _('world')

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        user = self.__create(email=email, password=password, **extra_fields)
        user.save(using=self._db)

        return user
