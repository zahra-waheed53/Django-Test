from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('product/add/', views.Addproduct, name='add_product'),
    path('product/<int:product_id>/update/', views.UpdateProduct, name='update_product'),
    path('product/<int:product_id>/delete', views.DeleteProduct, name='delete_product'),
    path('product/<int:product_id>/detail', views.ProductDetail, name='product_details'),
    path('product/logs', views.LogsList, name='log_list'),
]