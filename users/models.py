from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<username>/<filename>
    return '{0}/profile_picture/{1}'.format(instance.owner.username, filename)


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg',
                                        upload_to=user_directory_path)

    def __str__(self):
        return f'{self.owner.username}\'s Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
