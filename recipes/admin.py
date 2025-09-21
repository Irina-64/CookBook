from django.contrib import admin
from .models import Category, Ingredient, Recipe, RecipeIngredient, Comment, Rating


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    autocomplete_fields = ["ingredient"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "default_unit")
    search_fields = ("name",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "cook_time", "rating", "created_at")
    list_filter = ("category",)
    search_fields = ("title", "description")
    autocomplete_fields = ["author", "category"]
    inlines = [RecipeIngredientInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("recipe", "user", "created_at")
    search_fields = ("text",)
    autocomplete_fields = ["recipe", "user"]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("recipe", "user", "value", "created_at")
    list_filter = ("value",)
    autocomplete_fields = ["recipe", "user"]
