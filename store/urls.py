from django.urls import path
from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('pannacota/', views.pannacota, name="pannacota"),
	path('doughnut/', views.doughnut, name="doughnut"),
	path('dessertbox/', views.dessertbox, name="dessertbox"),
]