from django.db import models


class Url(models.Model):
    short_url = models.CharField(max_length=30)
    original_url = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url
