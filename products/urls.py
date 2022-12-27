from django.urls import path

app_name='products'
from . import views



urlpatterns=[ 
    path('product/',views.Product_view,name='product'),
    path('review/',views.Review_view,name='review'),
]