from django.db import models


class Category(models.Model):
    class Meta:
            verbose_name_plural = "categories"

    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=60)
    link = models.URLField(max_length=400)
    description = models.TextField()
    logo = models.URLField(max_length=200)
    categories = models.ManyToManyField(Category)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name) + " | " + str(self.approved)
