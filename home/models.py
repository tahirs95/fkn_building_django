from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    publish = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('Review-Detail', kwargs={'pk': self.pk})


class OurWorks(models.Model):
    title = models.CharField(max_length=25)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class WorkDone(models.Model):
    description = models.CharField(max_length=250)
    image = models.ImageField(default='default.jpg', upload_to='jobs_pics')
    publish = models.BooleanField(default=False)
    our_works = models.ForeignKey(OurWorks, on_delete=models.CASCADE)

    def __str__(self):
        return self.description






