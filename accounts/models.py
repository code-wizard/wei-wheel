from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from django.utils import timezone


class LtUser(AbstractBaseUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    email = models.EmailField(_('email address'), max_length=254, unique=True, db_index=True)
    username = models.CharField(_('username'), max_length=500, blank=True, unique=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = "lt_user"


class LtUserProfile(models.Model):
    user = models.OneToOneField(LtUser, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=16, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    # country =models.ForeignKey('cities_light.Country',null=True,blank=True)
    country = models.CharField(max_length=2, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(null=True, blank=True, max_length=50)
    gender = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = _("User Profile")
        db_table = "lt_user_profile"

