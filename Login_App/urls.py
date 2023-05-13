from django.urls import path
from Login_App import views

app_name = 'Login_App'


urlpatterns = [

    path('signup/', views.sing_up, name='sign_up'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('changeprofile/', views.user_change, name='userchange'),
    path('password/', views.pass_change, name='pass_change'),

]
