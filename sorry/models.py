from django.db import models
from django.utils import timezone
# Create your models here.


#  Relationship
# RELATIONSHIP = (
#     ('Ex-Lover', 'Ex-Lover'),
#     ('Family', 'Family'),
#     ('Significant Other', 'Significant Other'),
#     ('Friend', 'Friend'),
#     ('Co-Worker', 'Co-Worker'),
#     ('Stranger', 'Stranger'),
#
# )

RELATIONSHIP = (
    ('Ex-Lover', 'Ex-Lover'),
    ('Family', 'Family'),
    ('Significant Other', 'Significant Other'),
    ('Friend', 'Friend'),
    ('Enemy', 'Enemy'),
    ('Co-Worker', 'Co-Worker'),
    ('Stranger', 'Stranger'),

)


#sorry model
class Sorry(models.Model):
    title = models.CharField(max_length=30)
    relationship = models.CharField(max_length=17, choices=RELATIONSHIP)
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
