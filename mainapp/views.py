from django.shortcuts import render, redirect
from .forms import BuyForm
from django.utils import timezone
from .models import Region


def home(request):
    return render(request, 'KnightOne/index.html')


def portfolio_details(request):
    return render(request, 'KnightOne/portfolio_details.html')

def inner_page(request):
    return render(request, 'KnightOne/inner_page.html')

def about(request):
    return render(request, 'about/about.html')


def buy_new(request):
    if request.method == "POST":
        form = BuyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BuyForm()
    return render(request, 'temp/buy.html', {'form': form})