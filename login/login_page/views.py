from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Userregistrationform
from .models import profile
from django.http import JsonResponse

# Create your views here.
def registerform(request):

   if request.method=="POST":
       form = Userregistrationform(request.POST)

       if form.is_valid():
           form.save()
           username = form.cleaned_data['username']
           messages.success(request,f"{username} is sucessfully registered....login now")
           return redirect('login')


       else:
            return render(request,"login_page/register.html",{'form':form})

   form=Userregistrationform()
   return render(request, "login_page/register.html", {'form': form})


@login_required(login_url='login')
def account(request):
    return render(request,"login_page/account.html")

def account(request):
    return render(request,"login_page/account.html")

def details(request):
    return render(request,"login_page/details.html")

def jsonstock(request):
    st=profile.objects.all().values()
    st_list=list(st)
    return JsonResponse({'data':st_list})
