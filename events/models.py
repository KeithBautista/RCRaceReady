from django.db import models

# Create your models here.

# Model 3 Adding Events


class Event(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True)
    link = models.URLField(max_length=200)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True,
                            null=True)

    def __str__(self):
        return self.name
