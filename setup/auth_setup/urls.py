from django.urls import path
from . import views
app_name = 'auth'
urlpatterns = [
    path('', views.auth, name='auth'),
    path('create', views.auth_register, name='create'),
    path('login', views.auth_login, name='login'),
]
