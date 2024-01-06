from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('signup/',views.SigninView.as_view(),name='signup'),
    path('login/',views.user_login.as_view(),name='login'),
   # path('profile/',views.MyTemplateView.as_view(), name='profile'),
    path('teacherDashboard/', views.teacherDashboard, name='teacherDashboard'),
    path('certificate/', views.certificate_view, name='certificate_view'),
    path('mycourses/', views.MyCourses, name='mycourses'),
    path('create-announcement/', views.Announcement, name = 'create_announcement'),
    path('delete-announcement/<int:announcement_id>/', views.DeleteAnnouncement, name='delete_announcement'),
    path('player/<int:id>', views.VideoPlayerView.as_view(), name='player'),
]
