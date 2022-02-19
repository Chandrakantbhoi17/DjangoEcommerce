from django.contrib import admin

from .models import Product, SubCategory,Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name']



@admin.register(SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','sub_category_name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['prod_id1','prod_id2','subcategory','price','price_not','desc','gst','img']

   

