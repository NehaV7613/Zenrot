from django.conf import settings
from django.db import models

from django.utils import timezone

class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="tasks"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(default=timezone.now)  # Default value set to the current date
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_completed = models.BooleanField(default=False)
    proof_of_work = models.FileField(upload_to='proofs/', blank=True, null=True)  # Check if this field exists

    def __str__(self):
        return f"{self.title} ({self.user.username})"

