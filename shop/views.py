from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Customer, Category, Product, Cart, CartItem, Order, OrderItem
from .forms import CustomerForm, CategoryForm, CartItemForm, ProductForm

def home(request):
    return render(request, 'shop/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home') 
    else:
        form = RegistrationForm()
    return render(request, 'shop/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('shop:home.html')

#customer functions
# List all customers (for admin or authorized users)
#@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'shop/customer_list.html', {'customers': customers})

# View a single customer profile
#@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'shop/customer_detail.html', {'customer': customer})

# Create a new customer profile
#@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'shop/customer_form.html', {'form': form})

# Update an existing customer profile
#@login_required
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'shop/customer_form.html', {'form': form})

# Delete a customer profile
#@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'shop/customer_confirm_delete.html', {'customer': customer})

#products views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):  # Use pk for detail view
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'shop/product_confirm_delete.html', {'product': product})


def products_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/product_list.html', {'products': products, 'category': category})
#category 
# List all categories
#@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {'categories': categories})

# View a single category
#@login_required
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'shop/category_detail.html', {'category': category})

# Create a new category
#@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'shop/category_form.html', {'form': form})

# Update an existing category
#@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'shop/category_form.html', {'form': form})

# Delete a category
#@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'shop/category_confirm_delete.html', {'category': category})

#cart 
# View the cart
#@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'shop/cart_detail.html', {'cart': cart})

# Clear the cart
#@login_required
def cart_clear(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.items.all().delete()
    return redirect('cart_detail')

def cart_item_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if request.method == 'POST':
        form = CartItemForm(request.POST, instance=cart_item)
        if form.is_valid():
            cart_item.quantity = form.cleaned_data['quantity']
            cart_item.save()
            return redirect('cart_detail')
    else:
        form = CartItemForm(instance=cart_item)

    return render(request, 'shop/cart_item_form.html', {'form': form, 'product': product})

# Update a cart item
#@login_required
def cart_item_update(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if request.method == 'POST':
        form = CartItemForm(request.POST, instance=cart_item)
        if form.is_valid():
            form.save()
            return redirect('cart_detail')
    else:
        form = CartItemForm(instance=cart_item)

    return render(request, 'shop/cart_item_form.html', {'form': form, 'product': cart_item.product})

# Remove a cart item
#@login_required
def cart_item_remove(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart_detail')
