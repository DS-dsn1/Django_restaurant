from django.shortcuts import render, redirect
from .models import Chef, Dish, Customer
from .forms import DishForm


# Create your views here.
def index(request):
    return render(request,
                  'restaurant/index.html', )


def show_chef(request):
    chefs = Chef.objects.all()
    return render(request,
                  'restaurant/chefs.html',
                  {'chefs': chefs})


def dish_list(request):
    context = {'dish_list': Dish.objects.all()}
    return render(request, 'restaurant/dish_list.html', context)


def dish_form(request, id=0):
    # inside this will be insert and update operations
    if request.method == 'POST':
        if id == 0:
            form = DishForm(data=request.POST)
        else:
            dish = Dish.objects.get(pk=id)
            form = DishForm(data=request.POST, instance=dish)
        if form.is_valid():
            form.save()
        return redirect('/dish/list')
    else:
        if id == 0:
            form = DishForm()
        else:
            dish = Dish.objects.get(pk=id)
            form = DishForm(instance=dish)
        return render(request, 'restaurant/dish_form.html',
                      {'form': form})


def dish_delete(request, id):
    dish = Dish.objects.get(pk=id)
    dish.delete()
    return redirect('/dish/list')


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'restaurant/customer_list.html',
                  {'customers': customers})
