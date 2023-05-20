from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from Donor_App.models import Donations_Details
# Create your views here.


def Donor_dashboard(request):
    return render(request, 'Donor_App/Donor_Dashboard.html', context={})


class Donation_Create(LoginRequiredMixin, CreateView):
    model = Donations_Details
    template_name = 'Donor_App/Donate_form.html'
    fields = ('Amount', 'Phone', 'TrxID', 'Notes')
    form_submitted = False

    def form_valid(self, form: BaseModelForm):
        Donation_obj = form.save(commit=False)
        Donation_obj.Name = self.request.user
        Donation_obj.save()
        self.form_submitted = True
        dict = {'form': form, 'form_submitted': self.form_submitted}
        return render(self.request, 'Donor_App/Donate_form.html', context=dict)
