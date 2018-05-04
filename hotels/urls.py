from django.conf.urls import include, url
from . import views

app_name = 'hotels'

urlpatterns = [
   #package homepage
    url(r'^$',views.index2, name='index2'),

#details as hotels/id/
    url(r'^(?P<cities_id>[0-9]+)/$',views.details2,name='details2'),

    # hotels/id/bookings/
    url(r'^(?P<pk>[0-9]+)/hbookings/$', views.BookingsCreate.as_view(), name='bookings-create'),
# hotels/name/singleroom/
    url(r'^(?P<hname>[a-zA-Z0-9 ]+)/singleroom$', views.singleroom, name='singleroom'),

url(r'^(?P<hname>[a-zA-Z0-9 ]+)/doubleroom$', views.doubleroom, name='doubleroom'),

url(r'^(?P<hname>[a-zA-Z0-9 ]+)/multipleroom$', views.multipleroom, name='multipleroom'),

url(r'^(?P<hname>[a-zA-Z0-9 ]+)/familyroom$', views.familyroom, name='familyroom'),


 ]