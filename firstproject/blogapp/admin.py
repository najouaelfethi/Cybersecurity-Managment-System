from django.contrib import admin
from .models import Blog, Comment, Category
from embed_video.admin import AdminVideoMixin
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "status"]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Category)




class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


