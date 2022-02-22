from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)


class Expense(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    date = models.DateTimeField(blank=True)
    description = models.CharField(max_length=64)

    def __unicode__(self):
        return '{}-{}-{}'.format(self.username, self.amount, self.date)


class Income(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    date = models.DateTimeField(help_text='form : 2022-10-25 14:30')
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return '{}-{}-{}'.format(self.username, self.amount, self.date)
