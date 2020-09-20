from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    Vendor = 'VR'
    Garment = 'GM'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    category = models.CharField(max_length=20, choices=(
        (Vendor, 'Vendor'), (Garment, 'Garment')), default=Vendor)
    registration_num = models.IntegerField(default=0)
    address = models.CharField(max_length=150, default='')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_category(self):
        return self.category
