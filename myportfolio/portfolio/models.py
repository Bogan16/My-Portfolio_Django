from django.db import models

class ProfilePhoto(models.Model):
    image = models.ImageField(upload_to='profile_pictures/')