from django.conf.urls import include, url
from . import views

app_name = 'conveyance'

urlpatterns = [
   #package homepage
    url(r'^$',views.index3, name='index3'),

#details as hotels/id/
    url(r'^(?P<cities_id>[0-9]+)/$',views.details3,name='details3'),

    # hotels/id/bookings/
    url(r'^(?P<pk>[0-9]+)/renting/$', views.bookingscreate, name='bookingscreate'),

 ]