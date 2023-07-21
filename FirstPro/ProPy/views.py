
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>hello this is my home page</h1>")