from django.shortcuts import render
from .models import ProfilePhoto

def portfolio(request):
    profile_photo = ProfilePhoto.objects.first()
    return render(request, 'portfolio/portfolio.html', {'profile_photo': profile_photo})