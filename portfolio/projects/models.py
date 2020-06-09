from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 254)
    tagline = models.CharField(max_length = 1000,default="Enter a tagline")
    description = models.TextField()
    technology = models.CharField(max_length = 300,default="Enter a technology")
    cover_image = models.ImageField(blank=True)
    url = models.URLField(blank=True)
    screenshots = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length = 254)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.name
