from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# from phone_field import PhoneField
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from clarity import settings

from community.models import Community


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Please assign is_staff=True for superuser'))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                _('Please assign is_superuser=True for superuser'))
        return self.create_user(email, username, first_name, password, **other_fields)


# Create your models here.
class Custom(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(
        regex=r'^01[1|0|2|5][0-9]{8}$', message='phone must be an egyptian phone number...',)
    username = models.CharField(
        verbose_name="user_name", null=False, max_length=50)
    first_name = models.CharField(
        verbose_name="first_name", null=False, max_length=50)
    last_name = models.CharField(
        verbose_name="last_name", null=False, max_length=50)
    email = models.EmailField(verbose_name='email',
                              null=False, max_length=150, unique=True)
    phone = models.CharField(verbose_name="phone", null=True, validators=[
                             phone_regex], max_length=14)
    photo = models.ImageField(verbose_name="photo",
                              upload_to='users/images', null=True, blank=True)
    cover_photo = models.ImageField(verbose_name="photo",
                              upload_to='users/images', null=True, blank=True)
    community = models.ForeignKey(
        Community, on_delete=models.SET_NULL, null=True, blank=True)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL)
    is_active = models.BooleanField(default=True)
    bio = models.CharField(max_length=700,null=True,blank=True)
    date_birth = models.DateField(null=True)
    facebook_link = models.URLField(null=True)
    country = models.CharField(max_length=50, null=True)
    job_title = models.CharField(max_length=50, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']

    def get_user_community(self):
        return self.community

    def __str__(self):
        return self.username

    objects = CustomAccountManager()


class OnlineUser(models.Model):
    user = models.OneToOneField(Custom, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class FriendRequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_friend_requests')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_friend_requests')
    timestamp = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined')
    )
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=10)