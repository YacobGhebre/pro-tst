from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """docstring for Manager for User Profile."""

    def create_user(self, email, name, password=none):
    """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save super user"""

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
    # def __init__(self, arg):
    #     super(UserProfileManager, self).__init__()
    #     self.arg = arg




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """docstring for UserProfile. Database model for users in the system"""
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    is_staff = models..BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Retrieve string representation of our user"""
        return self.email

    #
    # def __init__(self, arg):
    #     super(UserProfile, self).__init__()
    #     self.arg = arg
