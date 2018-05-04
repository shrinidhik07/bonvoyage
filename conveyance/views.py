from django.views import generic
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import cities, vehicles,renting
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *

def index3(request):
    all_cities = cities.objects.all()
    context = {'all_cities': all_cities}
    return render(request, 'conveyance/index3.html', context)


# Create your views here.
def details3(request, cities_id):
    p = get_object_or_404(cities, pk=cities_id)
    return render(request, 'conveyance/details3.html', {'p': p})





def bookingscreate(request,pk):
    form = BookingsForm(request.POST or None)
    if form.is_valid():
        print(dict(request.POST), request.POST['name'])
        book = form.save(commit=False)
        #if len(request.POST['name']) < 3:
         #   return render(request, 'packages/form-template.html', {'error_messagenam': 'Enter correct contact info'})
        herename=get_object_or_404(vehicles,id=pk)
        book.vehicle_name =herename.vname
        book.save()

        if book is not None:
            print("yes ")
            return redirect('home:tests')
        else:
            print("not updated")
            form = BookingsForm()
            return render(request, 'conveyance/renting_form.html', {'error_message': 'Enter correct contact info'})
    else:
        print("not going")
        return render(request, 'conveyance/renting_form.html', {'error_message': 'Enter correct contact info'})


#class BookingsCreate(CreateView):
 #   model = renting
  #  fields = ['city','name', 'contact', 'email', 'starttime']



#def bookingscreate(request,pk):
 #   form = BookingsForm(request.POST or None)
  #  if form.is_valid():
   #     print(dict(request.POST), request.POST['name'])
    #    book = form.save(commit=False)
      #if len(request.POST['name']) < 3:
   #   return render(request, 'packages/form-template.html', {'error_messagenam': 'Enter correct contact info'})
     #   herename=get_object_or_404(vehicles,id=pk)
      #  book.vehicle_name =herename.vname
       # book.save()

        #   print("yes ")
         #   return redirect('home:tests')
        #else:
        #    print("not updated")
         #   form = BookingsForm()
          #  return render(request, 'conveyance/renting_form.html', {'error_message': 'Enter correct contact info'})
    #else:
     #   print("not going")
      #   return render(request, 'conveyance/renting_form.html', {'error_message': 'Enter correct contact info'})

