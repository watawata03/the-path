from django.contrib import admin
from .models import Work, Character, Route


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("title", "media_type", "beginner_level")


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ("title",)