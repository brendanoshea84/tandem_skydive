from django.shortcuts import render, redirect, reverse
from .forms import EnquirerForm
from django.core.mail import send_mail

# Create your views here.

def index(request):
    """Main page"""
    return render(request, 'home/index.html')

def day_plan(request):
    """A page to show a typical package time line"""
    return render(request, 'home/day-plan.html')

def contact_us(request):
    """A page for map and address/ email us"""
    form = EnquirerForm()
    context = {

        'form' : form,    
    }
    if request.method == 'POST':
        send_mail('Hello from SkyDive Goteborg',
        'We have recieved your question/message and one of our staff will response as quickly as possible',
        'projects4bos@gmail.com',
        ['b_oshea_84@hotmail.com'],
        fail_silently=False)
        return redirect(reverse('contact-us'))

    return render(request, 'home/contact-us.html', context)    
