from django.contrib import admin
from .models import course
# Register your models here.
@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','instructor']