from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dish_form, name='dish'),
    path('<int:id>/', views.dish_form, name='dish_update'),
    path('delete/<int:id>', views.dish_delete, name='dish_delete'),
    path('list/', views.dish_list, name='dish_list'),
]
