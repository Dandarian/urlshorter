from django.db import models
from hashlib import md5


class Link(models.Model):
    long_url = models.URLField(unique=True)
    short_url = models.URLField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.short_url = "http://" + \
                md5(self.long_url.encode()).hexdigest()[:10]

        return super().save(*args, **kwargs)
