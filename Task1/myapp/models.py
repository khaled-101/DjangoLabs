from django.db import models

# Create your models here.
class classroom(models.Model):
    name=models.CharField(verbose_name="Class",max_length=50 , unique=True)
    subject = models.CharField(verbose_name="Subject" , max_length=50)
    year = models.IntegerField(verbose_name="Year")
class classarea(models.Model):
    length=models.IntegerField(verbose_name="classlength")
    width=models.IntegerField(verbose_name="classlength")

