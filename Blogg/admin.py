from django.contrib import admin
from .models import*

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display =('title', 'slug', 'status','created_on')
    list_filter = ('status',)
    prepopulated_fields = {"slug":('title',)}


class BookAdmin(admin.ModelAdmin):
    list_display = ('name','image','author','price')
    list_filter = ('id')

admin.site.register(Profile)
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Author)
