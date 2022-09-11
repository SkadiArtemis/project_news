from django.contrib import admin
from .models import Post, Author, Category, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Category)
