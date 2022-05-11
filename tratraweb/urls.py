from django.urls import path
from . import views
from django.conf import settings

urlpatterns=[
path('',views.index,name='Home'),
path('donate',views.donation),
path('index.html',views.index),
path('Period',views.period),
path('education',views.education),
path('medical',views.medical),
path('submit',views.submit2)
]