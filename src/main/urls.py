from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.get_users, name='get_users'),
    path('err-test/', views.err_test, name='err_test'),
]
