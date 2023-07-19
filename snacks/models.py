from django.db import models
from accounts.models import CustomUser
from django.urls import reverse


# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length=255)
    purcheser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    url_image = models.TextField(default="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTVcKAm-JAZ7SMJEEoZyPfRu2qPYwIysAHNI6neFZlfZManK7Kx")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('snakslist')
