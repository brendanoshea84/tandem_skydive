from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import EnquirerForm
from django.core.mail import send_mass_mail
from django.contrib import messages
from profiles.models import UserProfile
# Create your views here.


def index(request):
    """Main page"""
    return render(request, 'home/index.html')


def day_plan(request):
    """A page to show a typical package time line"""
    return render(request, 'home/day-plan.html')


def contact_us(request):
    """A page for map and address/ email us"""
    if request.user.is_anonymous:
        form = EnquirerForm()
    else:
        profile = get_object_or_404(UserProfile, user=request.user)
        form = EnquirerForm(instance=profile)

    context = {
        'form': form,
    }

    name = request.POST.get('default_full_name')
    phone = request.POST.get('default_phone_number')
    email = request.POST.get('default_email')
    subject = request.POST.get('subject')
    question = request.POST.get('question')

    if request.method == 'POST':
        send_mail = (
            ('Hello from SkyDive Goteborg',
             'We have recieved your question/message about ' + subject +
             ' and one of our staff will response as quickly as possible!',
             'projects4bos@gmail.com',
             [email]),
            ('from ' + email + ' '+subject,
                'QUESTION ' + question + '/n PHONE: ' + phone,
                email,
                ['projects4bos@gmail.com'])
        )
        send_mass_mail(send_mail)
        messages.info(request, f'Thank-you {name}! We will return your email shorty!')
        return redirect(reverse('contact-us'))

    return render(request, 'home/contact-us.html', context)
