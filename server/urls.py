from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myapp.route.tutorialRoute')), 
    path('admin/', admin.site.urls),
]
