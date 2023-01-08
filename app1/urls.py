from django.urls import path

from .views import index, create, modify


urlpatterns = [
    path('', index, name='index'),
    path('criar/', create, name='criar'),
    path('modificar/<int:user_id>', modify, name='modify'),
]
