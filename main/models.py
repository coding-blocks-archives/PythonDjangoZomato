from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
  name = models.CharField(max_length = 256)
  address = models.TextField()
  contact = models.CharField(max_length = 64)
  veg_only = models.BooleanField(default = False)

  def __str__(self):
    return self.name

class Review(models.Model):
  restaurant = models.ForeignKey('Restaurant', on_delete = models.CASCADE)
  user = models.ForeignKey(User, on_delete = models.CASCADE)

  title = models.CharField(max_length = 256)
  body = models.TextField()
  # 0-5
  stars = models.IntegerField(validators=[
    MaxValueValidator(5),
    MinValueValidator(0)
  ])

  def __str__(self):
    return self.title
