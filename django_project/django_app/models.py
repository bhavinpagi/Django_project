import datetime

from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.FloatField(default=10)
    product_image = models.ImageField()
    active = models.BooleanField(default=True)
    rating = models.FloatField()
    available_quentity = models.IntegerField()
    pending_quentity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"Name : {self.product_name}, Discription: {self.product_description}, Rating: {self.rating}, Price: {self.price}"
    # def __int__(self):
    #     return f"Rating: {self.rating}"