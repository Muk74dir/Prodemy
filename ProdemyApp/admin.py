from django.contrib import admin
from .models import User, CourseCategoryModel, CourseModel

# Register your models here.
@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']

@admin.register(CourseCategoryModel)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(CourseModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','instructor']
    prepopulated_fields = {'slug': ('title',)}