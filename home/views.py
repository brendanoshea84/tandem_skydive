from django.shortcuts import render, redirect, reverse
from .forms import EnquirerForm
from django.core.mail import send_mass_mail
from django.contrib import messages

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
        'form': form,
    }

    Name = request.POST.get('Name')
    Email = request.POST.get('Email')
    Subject = request.POST.get('Subject')
    Question = request.POST.get('Question')

    if request.method == 'POST':
        send_mail = (
            ('Hello from SkyDive Goteborg',
             'We have recieved your question/message about ' + Subject +
             ' and one of our staff will response as quickly as possible!',
             'projects4bos@gmail.com',
             [Email]),
            ('from ' + Email + ' '+Subject,
                Question,
                Email,
                ['projects4bos@gmail.com'])
        )
        send_mass_mail(send_mail)
        messages.info(request, f'Thank-you {Name}! We will return your email shorty!')
        return redirect(reverse('contact-us'))

    return render(request, 'home/contact-us.html', context)
