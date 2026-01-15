from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('home/',views.home_view,name='home'),
    path('register/',views.register_user_view,name='register'),
    path('login/',views.login_user_view,name='login'),
    path('logout/',views.logout_view,name='logout')

]
