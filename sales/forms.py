from django import forms
from .models import BlogPost


class PostForm(forms.ModelForm):
    def clean(self):
        quantity = self.cleaned_data['quantity']
        inventory_item_quantity = self.cleaned_data['inventory_item']
        if quantity < inventory_item_quantity.quantity:  # order can be fulfilled
            print("Order placed!")
        else:
            raise forms.ValidationError({'quantity': "Not enough quantity to place an order."})
        print("sdfsdfsfsdffs")


class BlogPostFormView(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
