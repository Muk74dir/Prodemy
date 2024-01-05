from django.contrib import admin
from .models import User, CourseCategoryModel, CourseModel

# Register your models here.
@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']

@admin.register(CourseCategoryModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    
@admin.register(CourseModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','instructor']