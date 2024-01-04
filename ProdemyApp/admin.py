from django.contrib import admin
from .models import course,User

# Register your models here.
@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']

@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','instructor']