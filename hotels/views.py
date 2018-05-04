from django.views import generic
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import cities,accommodation,hbookings
from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import *

index=0
def index2(request):
    all_cities = cities.objects.all()
    context = {'all_cities': all_cities}
    return render(request, 'hotels/index2.html', context)

# Create your views here.
def details2(request, cities_id):
     p = get_object_or_404(cities, pk=cities_id)
     global index
     index=cities_id
     return render(request, 'hotels/details2.html', {'p': p})


class BookingsCreate(CreateView):
    model = hbookings
    fields = ['city','hotel_name','name','contact','email','Checkin','Checkout']
    exclude = ['bookintype','bookincost']


def singleroom(request,hname):
    form = SingleroomForm(request.POST or None)
    if form.is_valid():
        print(dict(request.POST), request.POST['name'])
        room = form.save(commit=False)
        # if len(request.POST['name']) < 3:
        #   return render(request, 'packages/form-template.html', {'error_messagenam': 'Enter correct contact info'})
        room.bookintype='Single bed'
        room.bookincost=1500
        global index
        room.city=str(cities.objects.get(id=index))
        decnum=accommodation.objects.get(hname=hname)
        decnum.sno-=1
        decnum.save()
        room.hotel_name=hname
        room.save()

        if room is not None:
            print("yes ")
            return redirect('home:tests')
        else:
            print("not updated")
            form = SingleroomForm()
            return render(request, 'hotels/singleroom.html', {'error_message': 'Enter correct contact info'})
    else:
        print("not going")
        return render(request, 'hotels/singleroom.html', {'error_message': 'Enter correct contact info'})



def doubleroom(request,hname):
    form = DoubleroomForm(request.POST or None)
    if form.is_valid():
        print(dict(request.POST), request.POST['name'])
        room = form.save(commit=False)
        # if len(request.POST['name']) < 3:
        #   return render(request, 'packages/form-template.html', {'error_messagenam': 'Enter correct contact info'})
        room.bookintype='Double bed'
        room.bookincost=2000
        global index
        room.city=str(cities.objects.get(id=index))
        decnum=accommodation.objects.get(hname=hname)
        decnum.sno-=1
        decnum.save()
        room.hotel_name=hname
        room.save()

        if room is not None:
            print("yes ")
            return redirect('home:tests')
        else:
            print("not updated")
            form = DoubleroomForm()
            return render(request, 'hotels/doubleroom.html', {'error_message': 'Enter correct contact info'})
    else:
        print("not going")
        return render(request, 'hotels/doubleroom.html', {'error_message': 'Enter correct contact info'})










def multipleroom(request,hname):
    form = MultipleroomForm(request.POST or None)
    if form.is_valid():
        print(dict(request.POST), request.POST['name'])
        room = form.save(commit=False)
        # if len(request.POST['name']) < 3:
        #   return render(request, 'packages/form-template.html', {'error_messagenam': 'Enter correct contact info'})
        room.bookintype='Multiple bed'
        room.bookincost=3000
        global index
        room.city=str(cities.objects.get(id=index))
        decnum=accommodation.objects.get(hname=hname)
        decnum.sno-=1
        decnum.save()
        room.hotel_name=hname
        room.save()

        if room is not None:
            print("yes ")
            return redirect('home:tests')
        else:
            print("not updated")
            form = MultipleroomForm()
            return render(request, 'hotels/multipleroom.html', {'error_message': 'Enter correct contact info'})
    else:
        print("not going")
        return render(request, 'hotels/multipleroom.html', {'error_message': 'Enter correct contact info'})


def familyroom(request, hname):
    form = FamilyroomForm(request.POST or None)
    if form.is_valid():
        print(dict(request.POST), request.POST['name'])
        room = form.save(commit=False)
        # if len(request.POST['name']) < 3:
        #   return render(request, 'packages/form-template.html', {'error_messagenam': 'Enter correct contact info'})
        room.bookintype = 'Family bed'
        room.bookincost = 2500
        global index
        room.city = str(cities.objects.get(id=index))
        decnum = accommodation.objects.get(hname=hname)
        decnum.sno -= 1
        decnum.save()
        room.hotel_name = hname
        room.save()

        if room is not None:
            print("yes ")
            return redirect('home:tests')
        else:
            print("not updated")
            form = FamilyroomForm()
            return render(request, 'hotels/familyroom.html', {'error_message': 'Enter correct contact info'})
    else:
        print("not going")
        return render(request, 'hotels/familyroom.html', {'error_message': 'Enter correct contact info'})











def singleroom(request,hname):
    form = SingleroomForm(request.POST or None)
    if form.is_valid():
        print(dict(request.POST), request.POST['name'])
        room = form.save(commit=False)
        # if len(request.POST['name']) < 3:
        #   return render(request, 'packages/form-template.html', {'error_messagenam': 'Enter correct contact info'})
        room.bookintype='Single bed'
        room.bookincost=1500
        global index
        room.city=str(cities.objects.get(id=index))
        decnum=accommodation.objects.get(hname=hname)
        decnum.sno-=1
        decnum.save()
        room.hotel_name=hname
        room.save()

        if room is not None:
            print("yes ")
            return redirect('home:tests')
        else:
            print("not updated")
            form = SingleroomForm()
            return render(request, 'hotels/singleroom.html', {'error_message': 'Enter correct contact info'})
    else:
        print("not going")
        return render(request, 'hotels/singleroom.html', {'error_message': 'Enter correct contact info'})