
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview, name='home_view'),
    path('contacts/',views.contact_view, name='home_view'),
    path('profile/',views.profile_view, name='home_view'),
    


]
