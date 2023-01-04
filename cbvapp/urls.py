from django.urls import path

app_name='cbvapp'
from . import views

urlpatterns=[ 
    path('order/',views.orderview,name='order'),
    path('cbvorder/',views.Cbvorderview.as_view(),name='cbvorder'),
    path('orderupdate/<pk>/',views.orderupdate,name='orderupdate'),
    path('cbvorderupdate/<pk>/',views.Cbvorderupdate.as_view(),name='cbvorderupdate'),
    path('cbvorderread/',views.Cbvorderread.as_view(),name='cbvorderread'),
    path('pcvcreate/',views.Pcvcreate.as_view(),name='pcvcreate'),
    path('pcvread/',views.Pcvlistview.as_view(),name='pcvread'),
    path('pcvdetail/<pk>/',views.Pcvdetailview.as_view(),name='pcvdetail'),
    path('pcvupdate/<pk>/',views.pcvupdateview.as_view(),name='pcvupdate'),
    path('pcvdelete/<pk>/',views.pcvdeleteview.as_view(),name='pcvdelete'),
    path('msg/',views.msg,name='msg'),

]