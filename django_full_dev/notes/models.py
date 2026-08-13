from django.db import models

# Create your models here.
class Note(models.Model):
    title =models.CharField(max_length=200)
    text=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    no_of_likes=models.PositiveIntegerField(default=0)