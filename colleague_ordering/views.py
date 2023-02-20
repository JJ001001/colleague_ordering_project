from django.shortcuts import render,redirect
from .forms import ColleagueForm
from .models import Colleague #import colleague class from models.py

# Create your views here.

def colleague_list(request):
    context = {'colleague_list':Colleague.objects.all()}# creates an object that imports all colleague
    return render(request, "colleague_ordering/colleague_list.html",context) #return all data records 

# CRUD INSERT OPERATION...SENDS FORM ENTRY TO DB

def colleague_form(request, id=0): #handles insert and update record
    if request.method == "GET":
        if id == 0:
            form = ColleagueForm()
        else:
            colleague = Colleague.objects.get(pk=id)
            form = ColleagueForm(instance= colleague)
        return render(request, "colleague_ordering/colleague_form.html", {'form':form})
    else:
        if id == 0:
            form = ColleagueForm(request.POST)
        else:
           colleague = Colleague.objects.get(pk=id)
           form = ColleagueForm(request.POST,instance= colleague) 
        if form.is_valid():
            form.save()
        return redirect('/colleague/list') #redirets user to /list after saving form      

def colleague_delete(request,id):
    colleague = Colleague.objects.get(pk=id)
    colleague.delete()
     #handles delete colleague record
    return redirect('/colleague/list')

''''
TRYING LOGIN

def collegue_login(request):
    return render(request, "colleague_ordering/login.html")
'''

def home(request):
    return render(request, "colleague_ordering/home.html")

def equipment_list(request):
    return render(request, "colleague_ordering/equipment_base.html")