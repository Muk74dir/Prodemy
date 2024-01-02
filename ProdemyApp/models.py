from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class course(models.Model):
    title           = models.CharField(max_length=200, unique=True)
    images          = models.ImageField(upload_to='photos/chobi',blank=False)
    description     = models.TextField(max_length=5000, blank=False)
    price           = models.IntegerField(default=0)
    created_date    = models.DateTimeField(auto_now_add=True)
    instructor      = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title
    