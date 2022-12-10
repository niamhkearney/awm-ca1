from django.contrib.gis import admin
from .models import WorldBorder, Profile, DogProfile

admin.site.register(WorldBorder, admin.GISModelAdmin)
admin.site.register(Profile)
admin.site.register(DogProfile)

