from django.urls import path
from credentials_app import views

urlpatterns = [

    path('/login',views.login,name='login.html'),
    path('/register', views.register, name='register.html'),
]
