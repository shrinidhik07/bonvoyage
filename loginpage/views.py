from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is a BONVOYAGE homepage</h1>")

# Create your views here.
