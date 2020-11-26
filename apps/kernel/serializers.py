from rest_framework import serializers

from apps.kernel import models


class FolderTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FolderTask
        fields = ('id', 'name', 'children', 'text')

    text = serializers.ReadOnlyField(source='name')

    def get_fields(self):
        fields = super().get_fields()
        fields['children'] = FolderTaskSerializer(many=True, required=False)
        return fields


class CommunicationObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommunicationObject
        fields = ('id', 'name', 'ip_address', 'port', 'state')


class PersonIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PersonIdentifier
        fields = ('id', 'name', 'kind', 'state')
