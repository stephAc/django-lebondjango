from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=150, null=False)
    price = models.DecimalField(max_digits=100000, decimal_places=2, null=False)
    description = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Date de parution")
    town = models.ForeignKey("Town", on_delete=models.SET_NULL, null=True)
    accepted = models.BooleanField(default=False)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    owner = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Articles"
        ordering = ["timestamp"]

    def __str__(self):
        return self.title

    def get_absolute_url_detail(self):
        return reverse("articles:detail", kwargs={"article_id": self.id})
