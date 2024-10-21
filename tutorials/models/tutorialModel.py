from django.db import models

class TutorialModel(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)

    class Meta:
        db_table = 'tutorial'  # Menetapkan nama tabel secara eksplisit
