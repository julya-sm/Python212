from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Register(models.Model):
    item = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item

