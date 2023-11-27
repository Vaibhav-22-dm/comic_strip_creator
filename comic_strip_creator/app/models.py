from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ComicStrip(models.Model):
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class ComicPanel(models.Model):
    comicstrip = models.ForeignKey(
        ComicStrip, null=True, blank=True, on_delete=models.CASCADE
    )
    image = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    prompt = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.comicstrip.prompt
