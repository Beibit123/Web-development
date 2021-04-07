from django.db import models


class Product(models.Model):
    name = models.CharField('name', max_length=10)
    price = models.FloatField('price')
    description = models.TextField('description')
    count = models.IntegerField('count')
    is_active = models.BooleanField('is_active')

    def __str__(self):
        return self.name

    def to_json(self):
        return{
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'price':self.price,
            'is_active':self.is_active,
            'count':self.count
        }


class Category(models.Model):
    name = models.CharField('name', max_length=10)

    def __str__(self):
        return self.name

    def to_json(self):
        return{
            'id':self.id,
            'name':self.name
        }