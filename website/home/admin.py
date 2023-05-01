from django.contrib import admin
from .models import fileupload, product, cart
# Register your models here.
admin.site.register(fileupload)
admin.site.register(product)
admin.site.register(cart)