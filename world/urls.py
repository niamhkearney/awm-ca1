from django.urls import path
from . import views

app_name = 'world'

urlpatterns = [
    path('', views.index, name='home'),
    path('maps/', views.maps, name='map'),
    path("signup/", views.register_request, name="signup"),
    path("locator/", views.location_request, name="locator"),
    path("moredog/", views.newdog_request, name="moredog"),
    path("dogs/", views.display_dogs, name="dogs"),
]