from django.db import models

# Create your models here.


class Gym(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    classes = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']