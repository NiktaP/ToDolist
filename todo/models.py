from datetime import timezone

from django.db import models
from django.utils import timezone
# Create your models here.

def one_week():
    return timezone.now() + timezone.timedelta(days=7)


class Todo(models.Model):
    id=models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    is_completed=models.BooleanField(default=False,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(default=one_week)
    last_update=models.DateTimeField(auto_now=True)


