from django.shortcuts import render

# Create your views here.

def index(request):
    """Main page"""
    return render(request, 'home/index.html')

def day_plan(request):
    """A page to show a typical package time line"""
    return render(request, 'home/day-plan.html')
