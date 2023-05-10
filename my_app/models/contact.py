from django.db import models


class Contact(models.Model):

    phone = models.CharField("Phone number", max_length=12)
    additionalPhone = models.CharField("Additional phone number", max_length=12)
    email = models.EmailField("Mail", max_length=50)
    working_mode = models.TextField("Working mode")
    place = models.OneToOneField("my_app.place", on_delete=models.CASCADE, related_name="contact")
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self) -> str:
        return f"Contacts {self.place}"