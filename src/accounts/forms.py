from pyexpat import model
from attr import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from accounts.models import CustomUser, Profile
from hotels.models import Chambre, Equipement, Equipement_Hotel, Hotel, Image_Chambre, Image_Hotel, Payement


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput())


class SigninForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    

class UserCreationForm(UserCreationForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(UserChangeForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name',
                  'is_active', 'is_admin','groups', 'user_permissions',)


class AddHotelImg(forms.ModelForm):
    class Meta:
        model = Image_Hotel
        fields = [
            'name',
            'image',

        ]


class EditHotel(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = [
            'name',
            'description',
            'tel_1',
            'tel_2',
            'email',
            'adress',
            'ville',
            'star_nbr',
        ]


class AddHotelEp(forms.ModelForm):
    class Meta:
        model = Equipement_Hotel
        fields = [
            'name',
            'number',
            'category',
        ]


class AddChambreEp(forms.ModelForm):
    class Meta:
        model = Equipement
        fields = [
            'name',
            'number',
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'tel',
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'gender',
            'birthdate',
            'country',
            'profile_pic',
            'update_at',
        ]

        Widgets = {'birthdate': forms.SelectDateWidget(
            years=range(1990, 2025))}


class ManagerEditChambre(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = [
            'number',
            'name',
            'description',
            'overnight',
            'area',
            'beds',
            'category',
            'capacity',
        ]


class AddChambreImg(forms.ModelForm):
    class Meta:
        model = Image_Chambre
        fields = [
            'name',
            'image',
        ]


class CheckBooking(forms.Form):
    secret_key = forms.CharField(min_length=6, required=True)


class DateInput(forms.DateInput):
    input_type = 'date'


class ManagerAddBooking(forms.Form):
    check_in = forms.DateField()
    check_out = forms.DateField()


class AddPayement(forms.ModelForm):
    class Meta:
        model = Payement
        fields = [
            'payment_method',
            'transaction_id',

        ]
