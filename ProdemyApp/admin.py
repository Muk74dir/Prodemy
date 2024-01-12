from django.contrib import admin
from .models import User, CourseCategoryModel, CourseModel, AnnouncementModel, QuestionModel, MCQModel

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
    
@admin.register(AnnouncementModel)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['person', 'course', 'title', 'description', 'image']


@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['person', 'course', 'title','description', 'file']

@admin.register(MCQModel)
class MCQAdmin(admin.ModelAdmin):
    list_display = ['question', 'option1','option2', 'option3', 'option4', 'answer']
    