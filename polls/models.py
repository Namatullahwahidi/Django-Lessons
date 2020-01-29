from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField



class Information(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class ProfileManager(models.Manager):
    def get_queryset(self):
        return super(ProfileManager, self).get_queryset().filter(city="Kandahar City")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image_original = models.ImageField(upload_to=user_directory_path,blank=True)
    image = ResizedImageField(size=[100, 100], crop=['middle', 'center'], upload_to=user_directory_path,
                              blank=True, null=True)



    # if we want to get ProfileManger we can call this object for example we can call only kandar city
    # kandar=ProfileManager()

    def __str__(self):
        return self.user.username


# make trigger for database
from django.db.models.signals import post_save


def create_profile(sender, **kewargs):
    if kewargs['created']:
        user_profile = Profile.objects.create(user=kewargs['instance'])


post_save.connect(create_profile, sender=User)
