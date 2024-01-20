from django import forms
from .models import PaymentMethod


class PaymentMethodForm(forms.ModelForm):
	class Meta:
		model = PaymentMethod
		fields = '__all__'
