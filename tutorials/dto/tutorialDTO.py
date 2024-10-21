from rest_framework import serializers 
from tutorials.models.tutorialModel import TutorialModel
 
 
class tutorialDTO(serializers.ModelSerializer):
 
    class Meta:
        model = TutorialModel
        fields = ('id',
                  'title',
                  'description',
                  'published')
