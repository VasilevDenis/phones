from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    try:
        sort = request.GET.get('sort')
        match sort:
            case 'max_price':
                phones = Phone.objects.order_by('-price')
            case 'min_price':
                phones = Phone.objects.order_by('price')
            case 'name':
                phones = Phone.objects.order_by('name')
    except Exception:
        phones = Phone.objects.order_by('name')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone':  Phone.objects.get(slug=slug)}
    return render(request, template, context)
