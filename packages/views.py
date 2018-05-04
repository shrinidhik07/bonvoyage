from django.views import generic
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import pcks,cityinfo,bookings
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import *
from django.http import HttpResponse


def index(request):
    all_pcks = pcks.objects.all()
    context = {'all_pcks': all_pcks}
    return render(request, 'packages/index.html', context)

# Create your views here.
def details(request, pcks_id):
     p = get_object_or_404(pcks, pk=pcks_id)
     return render(request, 'packages/details.html', {'p': p})


def registration_form(request):
    return render(request, 'packages/registration_form.html')

def bookingscreate(request,pk):
    form = BookingsForm(request.POST or None)
    if form.is_valid():
        print(dict(request.POST), request.POST['name'])
        book = form.save(commit=False)
        #if len(request.POST['name']) < 3:
         #   return render(request, 'packages/form-template.html', {'error_messagenam': 'Enter correct contact info'})
        herename=get_object_or_404(pcks,id=pk)
        book.package_name =herename.pname
        book.save()

        if book is not None:
            print("yes ")
            return redirect('home:tests')
        else:
            print("not updated")
            form = BookingsForm()
            return render(request, 'packages/bookings_form.html', {'error_message': 'Enter correct contact info'})
    else:
        print("not going")
        return render(request, 'packages/bookings_form.html', {'error_message': 'Enter correct contact info'})

#class BookingsUpdate(UpdateView):
 #   model = bookings
  #  fields = ['name','contact','email','start_date']


class UserFormView(View):
    form_class = UserForm
    template_name = 'packages/registration_form.html'

    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            #cleaned(normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if Credentials are correct
            user = authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return render(request,'home/tests.html')  #homepage redirection

        return render(request,self.template_name,{'form':form})



