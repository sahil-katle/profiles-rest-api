from django.db import models

# Standard base classes needed when overriding or customizing the default Django user model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles
    """   
    def create_user(self, email, name, password=None):
        """Create a new user profile
        """         
        if not email:
            raise ValueError('User mustr have am email address.')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save superuser with given details"""
        user = self.create_user(email, name, password) 

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system"""
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    # Will be used to determine is users profile is active
    is_active = models.BooleanField(default=True)
    # Will determine if user is staff user 
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieve full name of user
        """        
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user
        """        
        return self.name

    def __str__(self):
        """Return str representation of our user. Recommended for all django models 
        """        
        return self.email
    

