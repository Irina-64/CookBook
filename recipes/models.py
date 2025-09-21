from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)
    slug = models.SlugField("Слаг", max_length=120, unique=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Ingredient(models.Model):
    name = models.CharField("Название", max_length=150, unique=True)
    default_unit = models.CharField("Ед. изм. (по умолч.)", max_length=32, blank=True)

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipes",
        verbose_name="Автор",
    )
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание", blank=True)
    instruction = models.TextField("Инструкция")
    cook_time = models.PositiveIntegerField("Время приготовления (мин)")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recipes",
        verbose_name="Категория/сложность",
    )
    rating = models.DecimalField("Рейтинг", max_digits=3, decimal_places=2, default=0)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Изменено", auto_now=True)

    ingredients = models.ManyToManyField(
        Ingredient,
        through="RecipeIngredient",
        related_name="recipes",
        verbose_name="Ингредиенты",
    )

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient_recipes")
    amount = models.DecimalField("Количество", max_digits=8, decimal_places=2)
    unit = models.CharField("Ед. изм.", max_length=32, blank=True)

    class Meta:
        verbose_name = "Ингредиент рецепта"
        verbose_name_plural = "Ингредиенты рецепта"
        unique_together = ("recipe", "ingredient")

    def __str__(self):
        return f"{self.ingredient} — {self.amount} {self.unit}".strip()


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments", verbose_name="Рецепт")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments", verbose_name="Пользователь")
    text = models.TextField("Комментарий")
    created_at = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Комментарий от {self.user} к «{self.recipe}»"


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ratings", verbose_name="Рецепт")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ratings", verbose_name="Пользователь")
    value = models.PositiveSmallIntegerField("Оценка")  # 1..5
    created_at = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        ordering = ["-created_at"]
        unique_together = ("recipe", "user")

    def __str__(self):
        return f"{self.user} → {self.recipe}: {self.value}"
