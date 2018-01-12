from django.db import models
import datetime
#from Migration import fields


# Create your models here.
class Drug(models.Model):
    entry_date = models.DateTimeField(auto_now_add=True)
    Drug_name = models.CharField(max_length=225)
    Quantity = models.IntegerField()
    expire_date = models.DateField()

    def __str__(self):
        return self.Drug_name

class issued_Drug(models.Model):
    Drug_name = models.CharField(max_length=225)
    Quantity = models.IntegerField()

    def save(self):

        Drug.save(self)
        return self.Drug_name
