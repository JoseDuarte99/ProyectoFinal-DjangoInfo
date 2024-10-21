from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','author' ,'title', 'subtitle', 'date', 'text',
                    'active', 'category', 'image', 'published')


admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Comments)
