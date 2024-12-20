from django import forms
from .models import Customer, Category, Product, CartItem
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class CustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['user', 'phone_number', 'address', 'city', 'postal_code', 'country']

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ['name', 'slug']

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['category', 'name', 'slug', 'description', 'price', 'stock', 'image']

class CartItemForm(forms.ModelForm):
  class Meta:
    model = CartItem
    fields = ['quantity']