from django.shortcuts import render
from django.http import HttpResponse
from .models import Film
# Create your views here.
def wszystkie_filmy(request):
    #return HttpResponse('<h1>To jest nasz pierwszy test</h1>')
    test = 'To jest cos w views'
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'text': test, 'filmy': wszystkie})
