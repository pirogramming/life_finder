from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    nickname = models.CharField(max_length=15, verbose_name='닉네임')
    photo = models.ImageField(blank=True, upload_to="create_profile/%Y/%m/%d", verbose_name='프로필사진')
    age = models.IntegerField(blank=True, verbose_name='나이')
    job = models.CharField(blank=True, max_length=20, verbose_name='직업')
    description = models.TextField(blank=True, max_length=100,verbose_name='소개')
    goal_count = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
     )