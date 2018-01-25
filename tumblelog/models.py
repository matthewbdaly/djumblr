from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class TextPost(Post):
    text = models.TextField()


class ImagePost(Post):
    image = models.ImageField()


class LinkPost(Post):
    link = models.URLField()
