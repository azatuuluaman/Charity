from django.contrib import admin
from .models import Category, Donation, DonationImage, City, CategoryImage, Appeal
# from models import Callback, Collection, Image, Product, Cart, Order, CartItem


class ImageInline(admin.TabularInline):
    model = DonationImage
    max_num = 12
    min_num = 1
    extra = 0


class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    max_num = 12
    min_num = 1
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryImageInline, ]
    list_display = ('name', 'description')


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    list_display = ('title', 'categoryId', 'description', 'target', 'progress', 'charityQty', 'city', 'owner',
                    'phone_number', 'creation_date', 'end_date', 'requisites')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['title', ]


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'description', 'date']
