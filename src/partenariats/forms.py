from django import forms
from partenariats.models import Demandes


class RequestForm(forms.ModelForm):
    class Meta:
        model = Demandes
        fields = ('firstname', 'lastname', 'phone',
                  'email', 'etablishment_type',)
