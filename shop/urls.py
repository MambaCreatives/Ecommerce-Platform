from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'shop'  # Replace with your app's name

urlpatterns = [
    path('',views.home, name='home'),
    
    #auth
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), # Redirect to home after logout
    
    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/update/', views.customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    
    #product urls
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/<int:pk>/update/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('category/<int:category_id>/products/', views.products_by_category, name='products_by_category'),

    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Cart URLs
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
    path('cart/add/<int:product_id>/', views.cart_item_add, name='cart_item_add'),
    path('cart/update/<int:item_id>/', views.cart_item_update, name='cart_item_update'),
    path('cart/remove/<int:item_id>/', views.cart_item_remove, name='cart_item_remove'),
]