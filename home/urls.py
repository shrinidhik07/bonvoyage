from django.conf.urls import include, url
from . import views

app_name = 'home'

urlpatterns = [
   #package homepage
    url(r'^$',views.tests, name='tests'),


 ]