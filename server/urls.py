from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myapp.route.productRoute')), 
    path('', include('myapp.route.userRoute')), 
    path('admin/', admin.site.urls),
]
