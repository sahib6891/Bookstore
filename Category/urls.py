from django.conf.urls import url
from django.urls import path
from . import views
from .views import *

urlpatterns = [
		path('fiction/', views.fiction, name ='fiction'),
		path('horror/', views.horror, name ='horror'),
		path('suspense/', views.suspense, name ='suspense'),

		# url(r'^books/delete/(?P<pk>\d+)$', delete_view, name="delete_view"),



]
