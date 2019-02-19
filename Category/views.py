from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.generics import RetrieveAPIView, DestroyAPIView
from django.http import Http404
from Category.models import *
from django.http import HttpResponse
from .forms import *
from django.views.generic import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serialers import BooksSerializer,AuthorSerializer
from Bookstore.urls import *



# Create your views here.
@login_required(login_url="homepage")
def fiction(request):
    books = {}
    fiction_books = Books.objects.all().filter(category__exact='Fiction')
    books["booksdata"] = fiction_books
    return render(request, 'fiction.html', books)

@login_required(login_url="homepage")
def horror(request):
    books = {}
    horror_books = Books.objects.all().filter(category__exact='Horror')
    books["booksdata"] = horror_books
    return render(request, 'horror.html', books)

@login_required(login_url="homepage")
def suspense(request):
    # books = {"key3": ["Se7en", "The Usual Suspects", "psycho", "The Prestige", "Rear Window"]}
    # return render(request, 'suspense.html', books)

    books = {}
    suspense_books = Books.objects.all().filter(category__exact='Suspense')
    books["booksdata"] = suspense_books
    return render(request, 'suspense.html', books)


def delete_view(request, b_id):
    delete_data = Books.objects.get(id=b_id)
    delete_data.delete()
    return redirect("allbooks")

def delete_authorview(request,a_id):
    delete_author = Author.objects.get(id=a_id)
    delete_author.delete()
    return redirect("allauthors")

@login_required(login_url="homepage")
def add_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        print("hello world")
        if form.is_valid():
            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            publisher = form.cleaned_data['publisher']
            language = form.cleaned_data['language']
            year = form.cleaned_data['year']
            rating_user = form.cleaned_data['rating_user']
            price = form.cleaned_data['price']

            b = Books(title=title, category=category, publisher=publisher, language=language, year=year,
                    rating_user=rating_user, price=price)
            b.save()
            return redirect('allbooks')
        # print(title,category,publisher,language,year,rating_user,price)

    form = BookForm()
    return render(request, 'form.html', {'form': form})

@login_required(login_url="homepage")
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        print("Hello World")
        if form.is_valid():
            author_fname = form.cleaned_data['author_fname']
            author_lname = form.cleaned_data['author_lname']
            rating_user = form.cleaned_data['rating_user']

            a = Author(author_fname=author_fname, author_lname=author_lname, rating_user=rating_user)
            a.save()
            return redirect('allauthors')
    form = AuthorForm()
    return render(request, 'form.html', {'form': form})

# @login_required(login_url="homepage")
class assignauthor(TemplateView):
    login_required=True
    template_name = "assignauthor.html"

    def get(self,request):
        mylist = {}
        books = Books.objects.all()
        authordata = Author.objects.all()
        # books = Books.objects.all().values_list('title','id')
        mylist["booksdata"] = books
        mylist["authordata"] = authordata
        print(mylist)
        return render(request, 'assignauthor.html', mylist)
        # return render(request, 'assignauthor.html')

    def post(self,request):
        print(request.POST['authorid'])

        b = Books.objects.get(id=request.POST['bookid'])
        a = Author.objects.get(id=request.POST['authorid'])
        b.author_id = a
        b.save()
        # return render(request, "assignauthor.html")
        return redirect("allbooks")

def logout_view(request):
    logout(request)
    return redirect("homepage")

#List all books or create a new book
class BooksList(APIView):

    def get(self,request):
        books=Books.objects.all()
        serializer=BooksSerializer(books, many=True)
        return Response(serializer.data)

    # def delete(self,request,b_id):
    #     delete_book=get_object_or_404(Books,pk=b_id)
    #     # serializer=BooksSerializer(delete_book,many=True)
    #     delete_book.delete()
    #     return Response(status=status.HTTP_404_NOT_FOUND)

class AuthorList(APIView):

    def get(self,request):
        author=Author.objects.all()
        serializer=AuthorSerializer(author,many=True)
        return Response(serializer.data)
#
# class BooksDetail(APIView):
#
#     def get_object(self,b_id):
#         try:
#             return Books.objects.get(pk=b_id)
#         except Books.DoesNotExist:
#             raise Http404
#
#     def get(self,request,b_id,format=None):
#         snippet = self.get_object(b_id)
#         serializer = BooksSerializer(snippet)
#         return Response(serializer.data)
#
#     # def put(self, request, b_id, format=None):
#     #     snippet = self.get_object(pk=b_id)
#     #     serializer = BooksSerializer(snippet, data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self):
#         snippet=Books.get_object()
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)