# social_media/models.py
from django.db import models
from django.conf import settings
from tasks.models import Task

class SocialMediaSettings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    social_media_access = models.BooleanField(default=False)

    def check_social_media_access(self):
        # Fetch the user's pending tasks
        tasks = Task.objects.filter(user=self.user, is_completed=False)
        
        for task in tasks:
            current_time = timezone.now().time()

            # If task is completed or proof of work is uploaded, allow access
            if task.end_time < current_time or task.proof_of_work:
                self.social_media_access = True
                self.save()
                return True
        
        # Otherwise, deny access
        self.social_media_access = False
        self.save()
        return False
