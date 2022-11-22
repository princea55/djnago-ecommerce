from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    is_active = models.BooleanField(default=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    TYPE_CHOICES = (
        ('Customer', 'Customer'),
        ('Supplier', 'Supplier'),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print("sdfsdfsdfdfs")
        super(Customer, self).save(*args, **kwargs)

    class Meta:
        permissions = (("change_name", "can change name of product"),)