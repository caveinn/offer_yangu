from django.db import models
from offer_yangu.authentication.models import User

# Create your models here.
class Offers(models.Model):
  name_of_product =  models.CharField(max_length=255, unique=True)
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  stock = models.IntegerField()
  location = models.CharField(max_length=255)
  description = models.TextField()
  seller = models.ForeignKey(User, on_delete=models.CASCADE)
  previous_price = models.FloatField()
  current_price = models.FloatField()
  category = models.CharField(max_length=255)
