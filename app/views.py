from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def Student(request):
    STO=StudentForm()
    d={'STO':STO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('it is not valid data')

    return render(request,'Student.html',d)