from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product 
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError

def home(request):
	return render(request, 'products/home.html')


@login_required
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.POST['url']:
			product = Product()
			try:
				fm = request.FILES['image']
			except MultiValueDictKeyError:
				return render(request, 'products/create.html',{'error': 'Icono o image  no es incorrecto'})
			product.title = request.POST['title']
			product.body = request.POST['body']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
				product.url = request.POST['title']
			else:
				product.url = 'http://' + request.POST['url']
			product.pub_date = timezone.datetime.now()
			product.image = request.FILES['image']
			#product.icon = request.FILES['icon'] en caso de que quiera agerar un incono
			product.hunter = request.user
			product.save()
			return redirect('/products/' + str(product.id))
		else:
 			return render(request,'products/create.html'),{'error':'Todos los campos son necesarios'}
	else:
		return render(request, 'products/create.html')


def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render (request, 'products/detail.html', {'product':product})