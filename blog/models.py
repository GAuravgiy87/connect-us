from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

# 🔹 Room model to allow group-based document sharing
class Room(models.Model):
    room_id = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='rooms_joined')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms_created', null=True)  # Temporarily set null=True

    def __str__(self):
        return self.room_id

# 🔹 Post model with optional room-based sharing
class Post(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(null=True, blank=True, upload_to='Files')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)  # Optional room link

    def __str__(self):
        return self.title

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# 🔹 RoomFile model to store files uploaded within a specific room
class RoomFile(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Link to the room
    file = models.FileField(upload_to='room_files/')  # File uploaded to the room
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the file is uploaded
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Make this nullable to avoid migration errors

    def __str__(self):
        return f"File in room {self.room.room_id}"
