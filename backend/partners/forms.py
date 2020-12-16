from django import forms
from .models import Partner
#DataFlair

class PartnerCreate(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'