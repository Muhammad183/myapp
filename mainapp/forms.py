from django import forms
from .models import Buy


class BuyForm(forms.ModelForm):
    
    class Meta:
        model = Buy
        fields = ("first_name", "last_name", "phone_num",)