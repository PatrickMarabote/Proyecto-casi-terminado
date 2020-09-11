from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('imagenes',views.imagenes, name='imagenes'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
]