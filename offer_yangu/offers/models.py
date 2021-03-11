from django.db import models
from offer_yangu.authentication.models import User

# Create your models here.
class Offers(models.Model):
  name_of_product =  models.CharField(max_length=255, unique=True)
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  stock = models.IntegerField(null=True)
  location = models.CharField(max_length=255)
  description = models.TextField()
  seller = models.ForeignKey(User, on_delete=models.CASCADE)
  previous_price = models.FloatField()
  current_price = models.FloatField()
  category = models.ForeignKey("Category", verbose_name=("offer_category"), on_delete=models.CASCADE)
  image = models.ImageField(null=True)
  approved = models.BooleanField(default=False)


class Category(models.Model):
  name = models.CharField(max_length=255, unique=True)
