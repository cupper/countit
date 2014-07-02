from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_thumbs.db.models import ImageWithThumbsField

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    image = ImageWithThumbsField(upload_to='category_images', blank=True, sizes=((125,125), (25,25),))

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'id': self.id})


class Item(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category_list = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item', kwargs={'pk': self.pk})

    def get_category_list(self):
        return ", ".join([c.name for c in self.category_list.all()])
