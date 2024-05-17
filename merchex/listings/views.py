
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
	return HttpResponse("<h1>Hello Django!</h1>")


def about(request):
	return HttpResponse('<h1>A propos</h1> <p> A propos de nous</p>')


def listings(request):
	return HttpResponse('<h1>Listings</h1> <p>Supposed to be a list</p>')


def contact(request):
	return HttpResponse('<h1>Contact us</h1> <p> here is our contact</p>')

