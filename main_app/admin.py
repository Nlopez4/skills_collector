from django.contrib import admin
from .models import Mastered, gym, Skill
# Register your models here.
admin.site.register(gym)
admin.site.register(Skill)
admin.site.register(Mastered)
