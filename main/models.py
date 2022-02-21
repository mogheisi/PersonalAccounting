from django.contrib.auth.models import User
from django.db import models


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    description = models.CharField(max_length=256)
    def __unicode__(self):
        return '{}-{}-{}'.format(self.user, self.amount, self.date)


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    description = models.CharField(max_length=256)

