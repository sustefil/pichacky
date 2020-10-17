from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=32)  # TODO: Of course dude, this needs to be changed after testing

    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)

    def __str__(self):
        return self.username


class Place(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    default_lunchtime = models.SmallIntegerField(default=30)  # minutes

    def __str__(self):
        return f'{self.user}-{self.name}'


class Action(models.Model):
    class Type(models.TextChoices):
        CHECKIN = 'IN', _('Check-in')
        CHECKOUT = 'OUT', _('Check-out')

    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=Type.choices)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        unique_together = ('place', 'date', 'type')

    def __str__(self):
        return f'{self.place}_{self.type}_{self.date}_{self.time}'
