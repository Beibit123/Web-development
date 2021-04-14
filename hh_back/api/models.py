from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField('name', max_length=10)
    description = models.TextField('description')
    city = models.CharField('city', max_length=10)
    address = models.TextField('address')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'city':self.city,
            'address':self.address
        }


class Vacancy(models.Model):
    name = models.CharField('name', max_length=10)
    description = models.TextField('description')
    salary = models.FloatField('salary')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.name

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.name
        }