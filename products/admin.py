from django.contrib import admin

from .models import Category,Product,ProductFile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'avatar' , 'is_enable']
    list_filter = ['is_enable' , 'parent']
    search_fields = ['title']

class ProductFileInLineAdmin(admin.StackedInline):
    model = ProductFile
    field = ['title' , 'is_enable', 'file_type']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title' , 'avatar' , 'is_enable']
    list_filter = ['is_enable']
    search_fields = ['title']
    filter_horizontal = ['categories']
    inlines = [ ProductFileInLineAdmin ]


