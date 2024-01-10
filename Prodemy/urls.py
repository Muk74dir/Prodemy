from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.MyTemplateView.as_view(),name='home'),
    path('account/', include('ProdemyApp.urls')),
    path('payment/', include('transactions.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
