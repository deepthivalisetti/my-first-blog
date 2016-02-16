from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
        author = models.ForeignKey('auth.User')
        text = models.TextField()
        title = models.CharField(max_length=100)
        created = models.DateTimeField(default = timezone.now())
        published = models.DateTimeField(blank=True, null=True)

        def publish(self):
                self.published = timezone.now()
                self.save()

        def __str__(self):
                return self.title
