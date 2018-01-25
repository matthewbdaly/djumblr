from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.TextPost)
admin.site.register(models.ImagePost)
admin.site.register(models.LinkPost)
