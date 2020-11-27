from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='list'),
    path('view/<int:pk>', views.ProductView.as_view(), name='view'),
    path('new', views.ProductCreate.as_view(), name='new'),
    path('edit/<int:pk>', views.ProductUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', views.ProductDelete.as_view(), name='delete')
]