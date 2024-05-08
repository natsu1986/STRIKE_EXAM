from django.db import models
from django.contrib.auth.models import User

class task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datetobecomplete = models.DateTimeField(null=True, blank=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    urgent = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    pending_status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title