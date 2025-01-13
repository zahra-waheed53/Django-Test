from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)


class Logs(models.Model):
    ACTION_CHOICES = (
        ('CREATED', 'create'),
        ('UPDATED', 'update'),
        ('DELETED', 'delete')
    )
    action_performed = models.CharField(max_length=10, choices=ACTION_CHOICES)
    product_name = models.Foreignkey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    action_time = models.DateTimeField(auto_now_add=True)
