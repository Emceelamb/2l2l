from django.db import models
from django.utils import timezone
# Create your models here.

#sorry model
class Sorry(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    # published_date=models.DateTimeField(blank=True, null=True)
    # method to publish
    def publish(self):
        # self.published_date = timezone.now()
        self.title = self.title.lower()
        self.save()

    # method to return title
    def __str__(self):
        return self.title
