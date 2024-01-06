from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('signup/',views.SigninView.as_view(),name='signup'),
    path('login/',views.user_login.as_view(),name='login'),
    path('logout/',views.user_logout.as_view(),name='logout'),
    path('profile/<int:pk>',views.user_profile.as_view(),name='profile'),
    path('teacherDashboard/', views.teacherDashboard, name='teacherDashboard'),
    path('certificate/', views.certificate_view, name='certificate_view'),
    path('player/', views.VideoPlayerView.as_view(), name='player'),
]
