from django.urls import path

from interapp import views

urlpatterns = [

    path('',views.index,name='index'),
]