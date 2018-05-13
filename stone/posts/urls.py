from django.urls import path
from . import views

urlpatterns=[
    path('register',views.registerPost),
    path('prepare',views.prepare),
];