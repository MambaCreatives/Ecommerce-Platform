from django.contrib import admin
from .models import Customer, Category, Product, Cart, CartItem, Order, OrderItem

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)  # Might not be necessary for direct admin edits
admin.site.register(CartItem)  # Might not be necessary for direct admin edits
admin.site.register(Order)
admin.site.register(OrderItem)  # Might not be necessary for direct admin edits