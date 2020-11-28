from django.db import models

# Create your models here.
class BlogProject(models.Model):

    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=10000)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
