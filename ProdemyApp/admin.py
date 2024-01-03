from django.contrib import admin
from .models import course,User

# Register your models here.
admin.site.register(User)

@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','instructor']