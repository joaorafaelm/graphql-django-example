from django.contrib import admin
from bookstore.store.models import Author, Book, Publisher

admin.site.register([Author, Book, Publisher])
