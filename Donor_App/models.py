from django.db import models
from django.contrib.auth.models import User


class Donation_INFO(models.Model):
    Donator_name_id = models.ForeignKey(
        User, on_delete=models.CASCADE)

    Phone_Number = models.CharField(
        max_length=264, verbose_name="Phone no:", default='')
    TrxID = models.CharField(
        max_length=264, verbose_name="TrxID:", default='')
    Additional_Notes = models.TextField(
        verbose_name="Type some notes:", default='')
    Time_Of_Donate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Donator_name_id
