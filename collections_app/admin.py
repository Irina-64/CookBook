from django.contrib import admin
from .models import Collection, CollectionItem


class CollectionItemInline(admin.TabularInline):
    model = CollectionItem
    extra = 1
    autocomplete_fields = ["recipe"]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "is_public", "created_at")
    list_filter = ("is_public",)
    search_fields = ("title", "description")
    autocomplete_fields = ["owner"]
    inlines = [CollectionItemInline]


@admin.register(CollectionItem)
class CollectionItemAdmin(admin.ModelAdmin):
    list_display = ("collection", "recipe", "position")
    list_filter = ("collection",)
    autocomplete_fields = ["collection", "recipe"]
