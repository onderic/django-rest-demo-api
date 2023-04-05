from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data),
    path ('create', views.add_user),
    path ('read/<str:pk>', views.get_user),
    path ('update/<str:pk>', views.updateUser),
    path ('delete/<str:pk>', views.deleteUser),
]