from django.db import models

class Notes(models.Model):
    note_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()