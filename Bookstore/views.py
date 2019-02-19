from django.contrib.auth.decorators import login_required
from django.contrib.auth import *
from django.http import HttpResponse
from django.shortcuts import render
from Category.models import *
# from Category.models import Books
from django.contrib.auth.models import *
from Bookstore.urls import *
from Category.urls import *

def homepage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		print(username, password)
		if User.objects.filter(username=username).exists():
			login(request, user)
			return redirect('allbooks')

		else:
			return HttpResponse("<h1>Invalid Details</h1>")
	else:
		return render(request, 'homepage.html')


def contactus(request):
	return HttpResponse (" <h1> You can reach us at 999-999-9999 </h1> ")

@login_required(login_url="homepage")
def books(request):
	mylist ={}
	books = Books.objects.all()
	# books = Books.objects.all().values_list('title','id')
	mylist["booksdata"] = books
	return render(request,'books.html',mylist)

def authors(request):
	mylist1={}
	authors=Author.objects.all()
	mylist1["authorsdata"]=authors
	return render(request,'authors.html',mylist1)


