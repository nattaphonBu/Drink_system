from django.db import models

# Create your models here.
class TypeOfItem(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(default='', blank=True)
    price = models.IntegerField(default=0)
    create_at = models.DateTimeField('Start Date', null=True, blank=True)
    # create_by = models.ForeignKey(Account, on_delete = models.CASCADE)
    def __str__(self):
        return '%s' % self.name

class Tea(models.Model):
    drinkname = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    types = models.ForeignKey(TypeOfItem, on_delete = models.CASCADE)
    create_at = models.DateTimeField('Start Date', null=True, blank=True)
    # create_by = models.ForeignKey(Account, on_delete = models.CASCADE)
    def __str__(self):
        return '%s' % self.drinkname


class Account(models.Model):
    username = models.CharField(max_length = 30, blank=False)
    password = models.CharField(max_length = 30, blank=False)
    status = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % self.username



