from django.db import models

# Create your models here.
class fileupload(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField()
    body = models.TextField()
    soluong = models.FloatField()
    giaca = models.FloatField()
    def __str__(self):
        return self.title
class product(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    descripyion = models.TextField()
    def __str__(self):
        return self.name
class cart(models.Model):
    ImageField = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    number = models.CharField(max_length=12)