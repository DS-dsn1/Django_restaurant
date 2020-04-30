from django.contrib import admin
from .models import Chef, Dish, Customer, Orders, Payment


# Register your models here.
@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'experience', 'salary')
    search_fields = ('first_name', 'last_name')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'recipe', 'ingredients', 'cost')
    search_fields = ('name', )

