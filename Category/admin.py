from django.contrib import admin

from Category.models import *

# Register your models here.

admin.site.register(Books)      #super user shit
admin.site.register(Author)
