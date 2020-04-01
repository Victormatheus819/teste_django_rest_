from django.db import models


# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    def set_password(self, password):
        self.password=password