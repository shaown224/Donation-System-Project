from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Donation_Info(models.Model):
    Donor_Name= models.ForeignKey(User,on_delete=models.CASCADE,related_name="Donor_name")
    Donated_Amount = models.DecimalField(max_digits=10,decimal_places=2)
    Additional_Notes = models.CharField(max_length=140)
    Donation_Date =models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.Donor_Name + " " + self.Donated_Amount + " " + self.Additional_Notes + " " + self.Donation_Date