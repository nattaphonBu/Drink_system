from django.db import models

class Tea(models.Model):
    drinkname = models.CharField(max_length=255,blank=False)
    price = models.FloatField(default=0,blank=False)
    def __str__(self):
        return '%s' % self.drinkname

status_account=(
    ('Admin' ,'Admin'),
    ('Customer','Customer'),
    ('Employee','Employee')
)

class Account(models.Model):
    username = models.CharField(max_length = 30, blank=False)
    password = models.CharField(max_length = 30, blank=False)
    name = models.CharField(max_length = 50, blank=False, )
    tell = models.CharField(max_length = 10, blank=False, )
    status_account = models.CharField(max_length=30, choices=status_account, default='Customer')
    def __str__(self):
        return '%s' % self.username




class TypeOfItem(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(default='', blank=True)
    price = models.IntegerField(default=0)
    def __str__(self):
        return '%s' % self.name