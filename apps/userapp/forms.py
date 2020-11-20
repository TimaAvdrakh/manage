from django import forms

from apps.userapp.models import MainUser


class MainUserForm(forms.ModelForm):
    class Meta:
        model = MainUser
        fields = (
            'identifier', 'first_name', 'last_name', 'role', 'organization',
            'folder', 'is_active'
        )

    identifier = forms.CharField(label='Идентификатор')
    is_active = forms.BooleanField(widget=(forms.CheckboxInput), label='Статус')
