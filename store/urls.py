
from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

]

#from .views import login_view, products_view, home  # Import the home view

#urlpatterns = [
 #   path('', home, name='home'),  # URL pattern for the root path
  #  path('login/', login_view, name='login'),
   # path('/', products_view, name='index'),
    # Add other URL patterns for your application

