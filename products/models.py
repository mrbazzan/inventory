from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


def get_company_default_user():
    return get_user_model().objects.get(first_name='default')


class Product(models.Model):
    # Product name
    name = models.CharField(max_length=100, null=False)

    # Description of the product named above.
    description = models.TextField()

    # Company agent in-charge of delivering item.
    driver = models.ForeignKey('auth.User', on_delete=models.SET(get_company_default_user))

    # Location to which the product is to be delivered.
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
