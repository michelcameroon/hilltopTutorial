
from django.db import models

# Create your models here.


#from django.db import models


class OneTable(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField() 
    number = models.IntegerField()
    float = models.FloatField()
    decimal = models.DecimalField(max_digits=10, decimal_places=2)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
       return self.name


