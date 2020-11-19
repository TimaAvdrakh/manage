from django import forms

from apps.dictionary.models import Organization


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ('name', 'kind')
