from django.urls import path 
from pak.views import  *
app_name='pak'

urlpatterns=[
    path('babar/',babar,name='babar'),
    path('babar_bat/',babar_bat,name='babar_bat'),
]