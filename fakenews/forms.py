from django import forms
from django.contrib.auth import authenticate,get_user_model,login,logout

User = get_user_model()

class UserSignupForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password'
		]