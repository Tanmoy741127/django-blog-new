from django.contrib import admin
from .models import Post, Tag, Author, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('created_on', 'last_modified','author','tag')
    list_display = ('title', 'created_on', 'last_modified','author')
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_filter = ('created_on', 'post','user_name')
    list_display = ('user_name', 'text', 'created_on', 'post')
    

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)