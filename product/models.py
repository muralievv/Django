from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"{self.name}"

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='product/')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tag =  models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"{self.title}"



