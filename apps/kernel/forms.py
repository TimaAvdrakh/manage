from django import forms

from apps.kernel import models


class CommunicationObjectForm(forms.ModelForm):
    class Meta:
        model = models.CommunicationObject
        fields = ('id', 'name', 'ip_address', 'port', 'state')
