from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('contact_us', views.contact_us, name='contact_us'),
]