from django.db import models
from djongo.models import ListField, EmbeddedModelField


# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    des = models.TextField()
    # skills = ListField(EmbeddedModelField('Skill'))


# class Skill(models.Model):
#     skill_name = models.CharField(max_length=255)
#     level = ListField()
