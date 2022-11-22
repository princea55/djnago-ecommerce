from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.core.exceptions import ValidationError
from django import forms
# Create your models here.
from django.utils.translation import gettext
from django.dispatch import receiver
from django.urls import reverse


class Inventory(models.Model):
    item = models.CharField(max_length=20)
    item_code = models.IntegerField()
    item_condition = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item


class Order(models.Model):
    ord_number = models.CharField(max_length=20)
    inventory_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.ord_number


class PurchaseOrder(models.Model):
    ord_number = models.CharField(max_length=20)
    inventory_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    ordered_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.ord_number


def validate_order(sender, instance, **kwargs):
    if instance.quantity > instance.inventory_item.quantity:  # order can be fulfilled
        PurchaseOrder.objects.create(ord_number=f"P-{instance.ord_number}",
                                     inventory_item=instance.inventory_item,
                                     quantity=instance.quantity - instance.inventory_item.quantity
                                     )
    else:
        print("An order can not be place quantity is not enough to place an order.")
        pre_save.disconnect(validate_order, sender=sender)


pre_save.connect(validate_order, sender=Order)


@receiver(post_save, sender=Order)
def notify_user(sender, instance, **kwargs):
    print("post save is call", instance.ordered_by.username)


# post_save.connect(notify_user, sender=Order)


class BlogPost(models.Model):
    title = models.CharField(max_length=250, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail-view-blog', args=[str(self.id)])
