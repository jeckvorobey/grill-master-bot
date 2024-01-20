from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['user', 'address', 'name', 'update_at', 'created_at', 'deleted_at']
