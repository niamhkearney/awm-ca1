from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('maps/', views.maps, name='map'),
    path("signup/", views.register_request, name="signup"),
    path("locator/", views.location_request, name="locator"),
]