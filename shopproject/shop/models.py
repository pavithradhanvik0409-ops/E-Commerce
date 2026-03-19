from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_price = models.FloatField()
    product_image = models.ImageField(upload_to='products', null=True, blank=True)


    def __str__(self):
        return self.product_name

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name



