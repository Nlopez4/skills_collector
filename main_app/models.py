from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class gym(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    classes = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Skill(models.Model):
    technique = models.CharField(max_length=350)
    # class_took = models.CharField(max_length=150),    
    gyms = models.ForeignKey(
        gym, on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return self.technique
    
class Mastered(models.Model):
    belt = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill),
    
    def __str__(self):
            return self.belt


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_color = models.CharField(max_length=50)