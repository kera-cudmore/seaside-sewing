from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=254
    )
    friendly_name = models.CharField(
        max_length=254,
        blank=True,
        null=True,
    )

    def __Str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=254,
    )
    description = models.TextField(
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        null=True,
        blank=True,
    )
    quantity = models.PositiveSmallIntegerField(
    )
    colour = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
