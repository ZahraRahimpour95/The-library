from django.contrib import admin

from book.models import *

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','genre', 'price', 'publication_date', 'author', 'publisher')
    search_fields = ('title','author')
    

@admin.register(Authors)
class AuthorAdmin(admin.ModelAdmin):
    list_display =('id','first_name','last_name', 'birth_date')
    search_fields = ('last_name',)

@admin.register(Publishers)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id','name','city')



