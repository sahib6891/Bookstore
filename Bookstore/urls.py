"""Bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from Category import views as cview
from Category.views import *
# from Category.views import delete_view
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage,name='homepage'),
    path('contactus/', views.contactus),
    path('books/', views.books,name="allbooks"),
    path('books/', include('Category.urls')),
    path('books/delete/<int:b_id>', cview.delete_view,name="del"),
    path('addbooks/', cview.add_books,name="addbooks"),
    path('addauthor/', cview.add_author,name="addauthor"),
    # path('login/',cview.UserFormView.as_view(),name='login'),
    path('logout/',cview.logout_view,name='logout'),
    path('assignauthor',login_required(assignauthor.as_view()),name='assignauthor'),
    path('author',views.authors,name='allauthors'),
    path('author/delete/<int:a_id>', cview.delete_authorview,name="delauthor"),
    path('bjson/',BooksList.as_view(),name='bjson'),
    path('ajson/',AuthorList.as_view(),name='ajson'),
    # path('bjson/<int:b_id>',BooksDetail.as_view(),name='djson')
]

urlpatterns = format_suffix_patterns(urlpatterns)