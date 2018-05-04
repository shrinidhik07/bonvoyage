from django.conf.urls import include, url
from . import views

app_name = 'packages'

urlpatterns = [
   #package homepage
    url(r'^$',views.index, name='index'),

    #details as package/id/
    url(r'^(?P<pcks_id>[0-9]+)/$',views.details,name='details'),

    #package/id/bookings/
    url(r'^(?P<pk>[0-9]+)/bookings/$',views.bookingscreate,name='bookingscreate'),
    #url(r'^(?P<pcks_id>[0-9]+)/bookings/$',views.BookingsUpdate.as_view(),name='bookings-update'),


    #url(r'^accommodation/$', views.details2, name='details2'),

    #url(r'^accomodation/(?P<cities_id>[0-9]+)/$',views.details2,name='details2'),
    #url(r'^conveyance/',  include('conveyance.urls')),

    #url for registration form
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]