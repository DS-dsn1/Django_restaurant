from django import forms
from .models import Dish


class DishForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = '__all__'
        labels = {'name': 'Name of Dish'}
        field_classes = {
            'chefs': forms.ModelMultipleChoiceField,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipe'].required = False
        self.fields['ingredients'].required = False
