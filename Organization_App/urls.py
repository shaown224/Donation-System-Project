from django.urls import path

from Organization_App import views

app_name = 'Organization_App'
urlpatterns = [
    path('', views.Organization_dashboard, name='Organization_home'),
    path('donationlist/', views.Donation_list, name='donation_list'),
    path('donationslist/<int:id>', views.Details_Donations, name='DetailsDonation'),
    path('reporthome/', views.Report_home, name="report_home"),
    path('donatedbymonth/', views.Donated_by_month, name="donatemonth")

]
