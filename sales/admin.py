from django.contrib import admin
from .models import Inventory, Order, PurchaseOrder, BlogPost
from .forms import PostForm


class InventoryAdmin(admin.ModelAdmin):
    list_display = ("item", "item_code", 'item_condition', 'quantity')
    list_display_links = ("item_code",)


class OrderAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ("ord_number", "inventory_item", 'ordered_by', 'quantity')
    list_display_links = ("ord_number",)


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ("ord_number", "inventory_item", 'ordered_to', 'quantity')
    list_display_links = ("ord_number",)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by")
    list_display_links = ("title",)


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
