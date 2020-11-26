from django import forms
from django.utils.translation import ugettext_lazy as _

from apps.kernel import models


class FolderTaskForm(forms.Form):
    name = forms.CharField(label=_('name_tag'))
    parent = forms.IntegerField(label=_('paren_tag'), required=False)


class CommunicationObjectForm(forms.ModelForm):
    class Meta:
        model = models.CommunicationObject
        fields = ('id', 'name', 'ip_address', 'port', 'state')


class PersonIdentifierForm(forms.ModelForm):
    class Meta:
        model = models.PersonIdentifier
        fields = ('id', 'name', 'kind', 'state')
