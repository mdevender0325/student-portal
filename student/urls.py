
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.application, name='Home'),

    path('students/', include('news.urls')),
]
