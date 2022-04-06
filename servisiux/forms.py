from .models import OrderReview, Profile, Order
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = OrderReview
        fields = ('content', 'order', 'reviewer',)
        widgets = {'order': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']


class DateInput(forms.DateInput):
    input_type = 'date'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # fields = fields = '__all__'
        fields = ['car_instance_id', 'due_date']
        widgets = {
            'due_date': DateInput(), 'user': forms.HiddenInput(), 'date': forms.HiddenInput()}
            