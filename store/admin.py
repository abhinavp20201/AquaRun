from http.client import responses
from django.contrib import admin
from django.http import HttpResponse


from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order




class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone',]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['get_customer','address','phone','date','price','quantity','status']
    def get_customer (self,obj):
        return obj.customer.first_name
    get_customer.short_description='First_Name'


# Register your models here
# 
# 

    
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order,OrderAdmin)

#get name

