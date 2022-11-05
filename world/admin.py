from django.contrib.gis import admin
from .models import WorldBorder, Profile

admin.site.register(WorldBorder, admin.GISModelAdmin)
admin.site.register(Profile)

