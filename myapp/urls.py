from django.urls import path
from . import views 
urlpatterns = [
   path('hello',views.fnHello),
   path('sample',views.fnSample),
   path('sample2',views.fnSample2)
]