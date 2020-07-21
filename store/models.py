from django.db import models
from django.utils.translation import gettext_lazy as _

from jijiremix.utils import generate_random_token

# Create your models here.

def get_primary_key(prefix):
    return '{}_{}'.format(prefix, generate_random_token(6))

class ORMItem(models.Model):
    owner = models.ForeignKey('accounts.ORMUser', on_delete=models.CASCADE, related_name='owner')

    item_id = models.CharField(max_length=10, primary_key=True, blank=False, null=False, editable=False)
    name = models.CharField(max_length=20, blank=False, null=False, db_index=True)
    description = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    image = models.ImageField(upload_to="item_gallery/", default='item_gallery/dummy_img.jpg')

    is_sold = models.BooleanField(default=False)
    sold_to = models.ForeignKey('ORMBuyer', on_delete=models.CASCADE, null=True, blank=True, related_name='sold_to')

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def save(self, *args, **kwargs):
        if not self.item_id:
            self.item_id = get_primary_key('ITEM')
        return super(ORMItem, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.name)

class ORMBuyer(models.Model):
    item = models.ForeignKey(ORMItem, on_delete=models.CASCADE, related_name='item')
    name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField()
    location = models.CharField(max_length=20, blank=False)

    class Meta:
        verbose_name = 'Buyer'
        verbose_name_plural = 'Buyers'
    
    def __str__(self):
        return "{} <{}>".format(self.name, self.email)
