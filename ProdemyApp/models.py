from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from .constans import ACCOUNT_TYPE

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    AccounType = models.CharField(choices=ACCOUNT_TYPE,max_length = 20)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
class course(models.Model):
    title           = models.CharField(max_length=200, unique=True)
    images          = models.ImageField(upload_to='photos/chobi',blank=False)
    description     = models.TextField(max_length=5000, blank=False)
    price           = models.IntegerField(default=0)
    created_date    = models.DateTimeField(auto_now_add=True)
    instructor      = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title


class LectureNoteModel(models.Model):
    note_title = models.CharField(max_length = 50)
    course = models.ForeignKey(course, on_delete = models.CASCADE)
    instructor = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    content = models.FileField(upload_to='images/notes')