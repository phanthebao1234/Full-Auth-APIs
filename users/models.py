from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone 

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        email=self.normalize_email(email)
        email=email.lower()
        user = self.model(
            email=email,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(null=True, blank=True, default=timezone.now) 
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True) 
    date_joined = models.DateTimeField(default=timezone.now) 

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["last_name", "first_name"]

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None): 
        return self.is_superuser 
    
    def has_module_perms(self, app_label): 
        return self.is_superuser
