from django.db import models

# Standard base classes needed when overriding or customizing the default Django user model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles
    """   
    def create_user(self, email, name, password=None):
        """Create a new user profile
        """         
        if not email:
            raise ValueError('User must have am email address.')
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

class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.status_text
    

