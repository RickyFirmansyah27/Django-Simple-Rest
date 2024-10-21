from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tutorials.route.tutorialRoute')), 
    path('admin/', admin.site.urls),
]
