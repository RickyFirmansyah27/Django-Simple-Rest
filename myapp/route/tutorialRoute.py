from django.urls import path
from myapp.controller import tutorialController

urlpatterns = [
    path('api/tutorials', tutorialController.tutorial_list, name='tutorial-list'),
    path('api/tutorials/<int:pk>', tutorialController.tutorial_detail, name='tutorial-detail'),
    path('api/tutorials/published', tutorialController.tutorial_list_published, name='tutorial-list-published'),
]
