from django.urls import path

app_name='products'
from . import views



urlpatterns=[ 
    path('home/',views.HomePage,name='home'),
    path('product/',views.Product_view,name='product'),
    path('review/',views.Review_view,name='review'),
    path('proread/',views.ProductRead,name='proread'),
    path('reviewread/<pk>/',views.ReviewRead,name='reviewread'),
    path('proupdate/<pk>/',views.ProductUpdate,name='proupdate'),
    

]