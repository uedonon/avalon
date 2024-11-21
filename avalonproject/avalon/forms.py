from .models import Record
from django.forms import ModelForm, TextInput, DateInput


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['parent_fio', 'parent_phone', 'child_fio', 'child_dob']

        widgets = {
            'parent_fio': TextInput(attrs={'class': 'form-control custom-form-control', 'placeholder': 'Введите ваше ФИО'}),

            'parent_phone': TextInput(attrs={'class': 'form-control custom-form-control', 'id': 'parentPhone'}),

            'child_fio': TextInput(attrs={'class': 'form-control custom-form-control', 'placeholder': 'Введите ФИО ребенка'}),

            'child_dob': DateInput(attrs={'class': 'form-control custom-form-control', 'type': "date"}),
        }

class RecordSimpleForm(ModelForm):
    class Meta:
        model = Record
        fields = ['parent_fio', 'parent_phone', 'child_fio', 'child_dob']

        widgets = {
            'parent_fio': TextInput(attrs={'class': 'form-control custom-form-control', 'placeholder': 'Введите ваше ФИО'}),

            'parent_phone': TextInput(attrs={'class': 'form-control custom-form-control', 'id': 'parentPhone'}),
        }