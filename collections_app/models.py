from django.conf import settings
from django.db import models
from recipes.models import Recipe


class Collection(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="collections",
        verbose_name="Владелец",
    )
    title = models.CharField("Название коллекции", max_length=200)
    description = models.TextField("Описание", blank=True)
    is_public = models.BooleanField("Публичная", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class CollectionItem(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="items", verbose_name="Коллекция")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="in_collections", verbose_name="Рецепт")
    note = models.CharField("Заметка", max_length=255, blank=True)
    position = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Элемент коллекции"
        verbose_name_plural = "Элементы коллекции"
        unique_together = ("collection", "recipe")
        ordering = ["position", "id"]

    def __str__(self):
        return f"{self.collection} → {self.recipe}"
