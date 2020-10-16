from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=32)  # TODO: Of course dude, this needs to be changed after testing

    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)


class Place(models.Model):
    username = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    default_lunchtime = models.SmallIntegerField(default=30)  # minutes


class Action(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    type = models.CharField(max_length=32)
    timestamp = models.DateTimeField()
