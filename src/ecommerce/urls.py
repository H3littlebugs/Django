from django.urls import path
from ecommerce import views

urlpatterns = [
    path("", views.product_model_list_view, name='product-list'),  # Lista de productos
    path("product/<int:pk>/", views.product_model_detail_view, name='product-detail'),  # Detalle de un producto
    path("product/create/", views.product_model_create_view, name='product-create'),  # Crear un producto
    path("product/<int:pk>/update/", views.product_model_update_view, name='product-update'),  # Actualizar un producto
    path("product/<int:pk>/delete/", views.product_model_delete_view, name='product-delete'),  # Eliminar un producto
]
