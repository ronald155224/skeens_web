from django.contrib import admin
from products.models import Product, ProductCategory, ProductImage

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('name', 'image', 'order')

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category__name'] # 設定列表頁面查詢框
    fields = ('name', 'name_en', 'description', 'description_en', 'price', 'category', 'created', 'modified')
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    autocomplete_fields = ['category'] # 新增修改頁面關聯欄位查詢框
    readonly_fields = ('created', 'modified')
    inlines = [ProductImageInline, ]

class ProductCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name'] # 設定列表頁面查詢框
    fields = ('name', 'name_en', 'description', 'description_en', 'created', 'modified', 'image')
    list_display = ('name',)
    readonly_fields = ('created', 'modified')

admin.site.register(Product, ProductAdmin)         # 註冊 Product 模型
admin.site.register(ProductCategory, ProductCategoryAdmin)    # 註冊 ProductType 模型