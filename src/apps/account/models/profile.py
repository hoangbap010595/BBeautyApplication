from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='images/profiles/default.png',
        upload_to='images/profiles'
    )
    # status = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_profile'
        app_label = 'account'

    @property
    def image_url(self):
        return self.image.url

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        try:
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        except:
            print("error")
            pass
