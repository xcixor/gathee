from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


def get_default():
    """
    Get the default country code.
    Returns:
        code(object): default country code
    """
    return CountryCode.objects.get_or_create(
        country_code=254, country="Kenya")[0]


class CountryCode(models.Model):
    '''
    Country codes
    '''
    country_code = models.IntegerField(default=254, unique=True)
    country = models.CharField(max_length=255, default="Kenya", unique=True)

    def __str__(self):
        return "+" + str(self.country_code) + " " + self.country


class UserManager(BaseUserManager):
    """
    Interface for the User model for querying the database.
    """
    def _create_user(self, username, password=None, **extra_fields):
        """
        Create and save a user with the given email, password is not required.
        """
        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        """
        Create a user with a default country code if none is provided.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('phone_number', 726173014)
        if not extra_fields.get('country_code'):
            extra_fields.setdefault('country_code', get_default())
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Create a priviledged user of the site
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('phone_number', 726173014)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if not extra_fields.get('country_code'):
            extra_fields.setdefault('country_code', get_default())

        return self._create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """Creates a user of the application."""
    email = models.EmailField(
        _('email address'), unique=True,
        error_messages={'unique': _(
            "The email address you entered has already been registered.",), },
        max_length=255
        )
    username = models.CharField( _('username'), unique=True,
        error_messages={'unique': _(
            "The username address you entered has already been registered.",), },
        max_length=40)
    firstname = models.CharField(_('firstname'), max_length=30, blank=True)
    lastname = models.CharField(_('lastname'), max_length=30, blank=True)
    surname = models.CharField(_('surname'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date_joined'), default=timezone.now)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
            ),
        )
    is_active = models.BooleanField(
        _('active'), default=True, help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'),
        )
    is_change_allowed = models.BooleanField(
        _('change_allowed'), default=False, help_text=_(
            'Designates whether this user has been authorized to change '
            'his own password, in the change_password view.'),
        )
    country_code = models.ForeignKey(CountryCode, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    phone_number = models.IntegerField(blank=False, null=False)
    photo = models.ImageField(blank=True, null=True)
    change_email = models.EmailField(
        _('email address'), unique=True,
        error_messages={
            'unique': _(
                "The email address you entered has already been registered.",
                ),
            },
        max_length=255, default=None, blank=True, null=True
        )
    former_email = models.EmailField(_('email address'), max_length=255,
                                     default=None, blank=True,
                                     null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    # Require the email and password only
    REQUIRED_FIELDS = []


    def __str__(self):
        """Return a string representaion of the User object."""
        if self.firstname and self.surname:
            full_name = '%s %s' % (self.firstname, self.surname)
            return full_name.strip()
        elif self.firstname and self.lastname:
            full_name = '%s %s' % (self.firstname, self.lastname)
            return full_name.strip()
        elif self.surname and self.lastname:
            full_name = '%s %s' % (self.lastname, self.surname)
            return full_name.strip()
        return self.username
