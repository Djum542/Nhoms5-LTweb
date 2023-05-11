from django.db import models

from django.contrib.auth.models import User
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
    image = models.ImageField()
    name = models.CharField(max_length=200)
    price = models.FloatField()
    # descripyion = models.TextField()
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class cart(models.Model):
    ImageField = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    number = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    def __str__(self):
        return f"{self.quantity} x {self.product.product_id}"
class orders(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    product = models.ForeignKey(product, on_delete = models.SET_NULL, null=True, blank=False)
    def __str__(self):
        return self.name

