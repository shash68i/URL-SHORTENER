from django.db import models


class Url(models.Model):
    short_url = models.CharField(max_length=30, verbose_name='')
    original_url = models.CharField(max_length=1000, verbose_name='')
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        '''
        This function is to store exact url, even if user fails to do so
        '''
        HTTPS = 'https://'
        HTTP = 'http://'
        WWW = 'www.'
        if (not self.original_url.startswith(HTTPS) and
                not self.original_url.startswith(HTTP)):
            if self.original_url.startswith(WWW):
                self.original_url = HTTPS + self.original_url
            else:
                self.original_url = HTTPS + WWW + self.original_url
        super(Url, self).save(*args, **kwargs)

    def __str__(self):
        return self.short_url
