from django.shortcuts import render

# Create your views here.
def store(request):
	context = {}
	return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)

def pannacota(request):
	context = {}
	return render(request, 'store/pannacota.html', context)

def doughnut(request):
	context = {}
	return render(request, 'store/doughnut.html', context)

def dessertbox(request):
	context = {}
	return render(request, 'store/dessertbox.html', context)
