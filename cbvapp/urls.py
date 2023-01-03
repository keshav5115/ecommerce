from django.urls import path

app_name='cbvapp'
from . import views

urlpatterns=[ 
    path('order/',views.orderview,name='order'),
    path('cbvorder/',views.Cbvorderview.as_view(),name='cbvorder'),
    path('orderupdate/<pk>/',views.orderupdate,name='orderupdate'),
    path('cbvorderupdate/<pk>/',views.Cbvorderupdate.as_view(),name='cbvorderupdate'),
    path('cbvorderread/',views.Cbvorderread.as_view(),name='cbvorderread'),
]