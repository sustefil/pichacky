from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('err-test/', views.err_test, name='err_test'),
]
