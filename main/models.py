from django.db import models


class Category(models.Model):
    class Meta:
            verbose_name_plural = "categories"

    name = models.CharField(max_length=60, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=60, blank=False)
    link = models.URLField(max_length=400, blank=False)
    description = models.TextField(blank=False)
    categories = models.ManyToManyField(Category)
    approved = models.BooleanField(default=False)
    is_for_developers = models.BooleanField(default=False)
    is_beta = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + " | " + str(self.approved)
