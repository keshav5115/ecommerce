from django.urls import path

app_name='customer'
from . import views

urlpatterns=[ 
    path('customer/',views.CustomerView,name='customer'),
]