from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    birthday = models.DateField()

    def __unicode__(self):
        return u'%s' % (self.name)


class Telefon(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    number = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % (self.number)

