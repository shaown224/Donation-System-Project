from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import CreateView, View
from Donor_App.models import Donation_INFO
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def Donor_dashboard(request):
    return render(request, 'Donor_App/Donor_Dashboard.html', context={})


class CreateDonation(LoginRequiredMixin, CreateView):
    model = Donation_INFO
    template_name = 'Donor_App/Donate_form.html'
    fields = {'Amount', 'Phone_Number', 'TrxID', 'Additional_Notes', }
