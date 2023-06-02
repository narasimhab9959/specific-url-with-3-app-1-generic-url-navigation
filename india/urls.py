from django.urls import path 
from india.views import *
app_name='india'

urlpatterns=[
    path('kohli/',kohli,name='kohli'),
    path('kohli_bat/',kohli_bat,name='kohli_bal'),
]