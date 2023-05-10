from django.db import models


class Category(models.Model):

    title = models.CharField("Title", max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title