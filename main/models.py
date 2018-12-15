from django.db import models


class Category(models.Model):
    class Meta:
            verbose_name_plural = "categories"

    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=60)
    link = models.URLField(max_length=400)
    description = models.TextField()
    logo = models.URLField(max_length=200)
    categories = models.ManyToManyField(Category)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + " | " + str(self.approved)