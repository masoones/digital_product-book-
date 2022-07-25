from django.urls import path

from .views import (
    ProductListView,CategoryListView,ProductFileListView,
    ProductDetailListView,CategoryListView,ProductFileDetailListView,
)


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='category-detail'),

    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailListView.as_view(), name='product-detail'),

    path('products/<int:product_id>/files/', ProductFileListView.as_view(), name='file-list'),
    path('products/<int:product_id>/files/<int:pk>/', ProductFileDetailListView.as_view(), name='file-detail'),
]