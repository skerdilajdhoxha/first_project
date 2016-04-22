from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'published']
    list_display_links = ['title']
    search_fields = ['title', 'content']
    prepopulated_fields = {"slug": ("title",)}
    #view_on_site = True
    #list_editable = ['author']
    list_per_page = 5
    list_filter = ['title', 'created']
    #view_on_site = True


admin.site.register(Post, PostAdmin)
