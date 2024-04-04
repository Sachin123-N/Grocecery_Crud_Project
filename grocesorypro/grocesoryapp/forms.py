from django import forms
from .models import Grocesory


class GrocesoryForm(forms.ModelForm):
    class Meta:
        model = Grocesory
        fields = "__all__"

        widgets = {
            "shop_name": forms.TextInput(attrs={'class': 'class-controls'}),
            "total_price": forms.NumberInput(attrs={'class': 'class-controls'}),
            "flat_no": forms.NumberInput(attrs={'class': 'class-controls'}),
            "discout_price": forms.NumberInput(attrs={'class': 'class-controls'}),
            "payment_mode": forms.Select(attrs={'class': 'class-controls'}),
        }
