from django.contrib import admin

from .models import Author, Tag, Post, Comment


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address")


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", "date")
    list_display = ("title", "date", "author")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")


# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

