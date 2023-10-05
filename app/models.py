from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class Thing(AbstractUser):
	name = models.CharField(max_length = 50)
	description = models.TextField(max_length = 300)
	quantity = models.IntegerField()