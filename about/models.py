from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')
    # class Meta:
    #     ordering = ['-created_on']

    def __str__(self):
        return f"{self.title}"


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
