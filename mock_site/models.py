from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

# Create your models here.
class Session(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField()
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    #Added an email field and UUID field. Haven't migrated yet.
    invitee_email = models.EmailField(default="example@email.com")
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('session-detail', kwargs={'pk': self.pk})
