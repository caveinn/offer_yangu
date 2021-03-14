from django.contrib import admin
from .models import Category, Offers, Location

# Register your models here.
admin.site.register(Offers)
admin.site.register(Category)
admin.site.register(Location)
