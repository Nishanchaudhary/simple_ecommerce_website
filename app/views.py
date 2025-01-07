from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def base_view(request):
    return render(request, 'layout/base.html')

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def shop(request):
    # Get sorting option
    sort = request.GET.get('sort', 'price_asc')
    sort_options = {
        'price_asc': 'price',
        'price_desc': '-price',
        'name_asc': 'name',
        'name_desc': '-name',
    }
    sort_field = sort_options.get(sort, 'price')

    # Fetch and sort products
    products_list = Product.objects.all().order_by(sort_field)

    # Pagination
    paginator = Paginator(products_list, 8)  # Show 8 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'shop.html', {'products': products})

@csrf_exempt  # Use this only for demo purposes; implement CSRF protection in production
def add_to_cart(request):
    if request.method == "POST":
        # Get the cart (or create if not existing)
        cart, created = Cart.objects.get_or_create(id=1)  # Assuming single cart system
        cart.item_count += 1
        cart.save()
        return JsonResponse({"item_count": cart.item_count})
    return JsonResponse({"error": "Invalid request"}, status=400)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')