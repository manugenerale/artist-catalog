from django.contrib import admin

# Register your models here.

from artist_catalog.models import Artiste, Oeuvre

admin.site.register(Artiste)
admin.site.register(Oeuvre)
