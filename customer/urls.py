from django.urls import path

app_name='customer'
from . import views

urlpatterns=[ 
    path('customer/',views.CustomerView,name='customer'),
    path('login/',views.CustomerLogin,name='login'),
    path('logout/',views.CustomerLogout,name='logout'),
]