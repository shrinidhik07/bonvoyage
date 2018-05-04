from django.views import generic
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render,redirect
from django.views.generic import View



def tests(request):
    return render(request, 'hotels/tests.html')

# Create your views here.
