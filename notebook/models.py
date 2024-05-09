from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Notebook(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)

    PRIORITY_CHOICES = (
        ("low", "Niski"),
        ("medium", "Średni"),
        ("high", "Wysoki")
    )

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Opublikowany')
    )

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="low")
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notebooks')

    class Meta:
        ordering = ('high','-publish')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('djangoProject:notes_detail', args=[self.publish.year,
                                                 self.publish.month, self.publish.day,
                                                 self.slug])