from django.db import models
from datetime import datetime
from .helpers import private_url_maker

# Create your models here.
class GhostPost(models.Model):
    boast = models.BooleanField()
    text = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    private_url = models.CharField(max_length=6)
    datetime = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.text
    
    def score(self):
        return (self.upvotes - self.downvotes)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.upvotes = 0
            self.downvotes = 0
            self.private_url = private_url_maker()

        super(GhostPost, self).save(*args, **kwargs)
