from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    #url(r'^packages/', include('packages.urls')),
    #url(r'^customisedpackages/', include('customisedpackages.urls')),
]