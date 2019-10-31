from django.db import models
from django.contrib.auth.models import User

class Clients(models.Model):

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others")
    ]

    name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, blank=False)
    phone = models.CharField(max_length=11, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    zip_code = models.CharField(max_length=8, null=False, blank=False)
    street = models.CharField(max_length=256, null=False, blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.name