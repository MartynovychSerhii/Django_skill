from django.db import models

# Create your models here.
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title