from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('signup/',views.SigninView.as_view(),name='signup'),
   # path('login/',views.MyTemplateView.as_view(),name='login'),
   # path('profile/',views.MyTemplateView.as_view(), name='profile'),
]
