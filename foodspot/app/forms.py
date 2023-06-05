from django import forms
from .models import restaurant_details

#create form restaurant signup
class Restaurant_signup_form(forms.ModelForm):
	class Meta:
		model = restaurant_details
		fields=[
			'restaurant_name',
			'password',
			'email',
			'state',
			'city',
			'address',
			'phnnumber',
			'about_restaurant',
			'logo']