from django.contrib import admin

from .models import Author, Tag, Post


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address")


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "date", "author")
    
    


# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
