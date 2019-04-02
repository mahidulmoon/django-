from django.shortcuts import render,redirect
from .forms import UserRegister
from django.contrib import messages
# Create your views here.
def main_page(request):
    return render(request,'user/welcome_page.html')

def register(request):
    if request.method=="POST":
        form=UserRegister(request.POST)
        if form.is_valid():
            form.save()

            return redirect('welcome_page')
    else:
        form=UserRegister()
    return render(request,'user/register.html',{'form':form})

