from django.db import models
from django.contrib.auth.models import User


class Donations_Details(models.Model):
    Name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="name")
    Amount = models.CharField(max_length=264, verbose_name="Give the Amount")
    Phone = models.CharField(max_length=264, verbose_name="Phone NO")
    TrxID = models.CharField(max_length=264, verbose_name="TrxID")
    Notes = models.TextField(verbose_name="Say something")
    Time = models.DateTimeField(auto_now_add=True)

    def Donator_name(self):
        return self.Name
