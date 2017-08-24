from django.db import models

# Create your models here.

#sorry model
class Sorry(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()

    # method to publish
    def publish(self):
        self.save()

    # method to return title
    def __str__(self):
        return self.title
