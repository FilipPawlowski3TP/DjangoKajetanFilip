from django.db import models

# Create your models here.
class Notebook(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    PRIORITY_CHOICES = (
        ("low", "Niski"),
        ("medium", "Średni"),
        ("high", "Wysoki")
    )

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="low")
