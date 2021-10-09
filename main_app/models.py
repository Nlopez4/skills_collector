from django.db import models

# Create your models here.


class gym(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    classes = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Skill(models.Model):
    technique = models.CharField(max_length=350)
    class_took = models.CharField(max_length=150)
    gyms = models.ForeignKey(
        gym, on_delete=models.CASCADE, related_name="skills")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.technique
