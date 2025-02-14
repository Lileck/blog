from django.contrib import admin

# Register your models here.
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Donats)
class DonatsAdmin(admin.ModelAdmin):
    ...
    
 @admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...
    
