from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=100, null=False)
    name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=True)
    number = models.CharField(max_length=10, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
