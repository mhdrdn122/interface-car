from django.db import models


class SignIn(models.Model):
    username = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20  , null=True)

    def __str__ (self):
        return self.username

    

# Create your models here.
