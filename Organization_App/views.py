from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from Donor_App.models import Donations_Details

# Create your views here.


def Organization_dashboard(request):
    return render(request, 'Organization_App/Organization_home.html', context={})


def Donation_list(request):
    obj = Donations_Details.objects.order_by('-Time').all()
    return render(request, 'Organization_App/Donator_list.html', {'obj': obj})


def Details_Donations(request, id):
    obj = get_object_or_404(Donations_Details, pk=id)
    return render(request, 'Organization_App/Detail_of_Donation.html', {'obj': obj})


def Report_home(request):
    return render(request, 'Organization_App/Reports_Generate_home.html', context={})


def Donated_by_month(request):
    obj = Donations_Details.objects.all()
    return render(request, 'Organization_App/Donated_by_month.html', {'obj': obj})
