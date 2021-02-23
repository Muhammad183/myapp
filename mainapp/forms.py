from django import forms
from .models import Buy, Document


class BuyForm(forms.ModelForm):
    
    class Meta:
        model = Buy
        fields = ("first_name", "last_name", "phone_num",)



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )