from django.urls import path
from BeeBlissApp import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('quality/', views.quality, name='quality'),
    path('shop/', views.shop, name='shop')
]