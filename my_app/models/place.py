from django.db import models


class Place(models.Model):

    title = models.CharField("Title", max_length=120)
    description = models.TextField("Description", null=True)
    city = models.ForeignKey("my_app.city", on_delete=models.CASCADE, related_name="city", verbose_name="City")
    address = models.CharField("Address", max_length=300)
    categories = models.ForeignKey("my_app.category", verbose_name="Categories", on_delete=models.CASCADE, related_name="category")
    create_time = models.DateTimeField("Created_at", auto_now_add=True)
    update_time = models.DateTimeField("Updated_at", auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Institutions"
        verbose_name_plural = "institution"

    def __str__(self) -> str:
        return self.title
