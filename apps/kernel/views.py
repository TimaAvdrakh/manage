from rest_framework import viewsets, mixins, views
from rest_framework.response import Response

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from apps.kernel import (
    serializers,
    models,
    forms,
)


class IndexView(TemplateView):
    template_name = 'kernel/index.html'


class CommunicationObjectView(ListView):
    template_name = 'kernel/communication_object/index.html'
    model = models.CommunicationObject
    context_object_name = 'communication_objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_obj'] = forms.CommunicationObjectForm
        return ctx


class CommunicationObjectViewAPI(mixins.RetrieveModelMixin,
                                 viewsets.GenericViewSet):
    model = models.CommunicationObject
    serializer_class = serializers.CommunicationObjectSerializer
    queryset = models.CommunicationObject.objects.all()


class CommunicationObjectCreateView(CreateView):
    model = models.CommunicationObject
    form_class = forms.CommunicationObjectForm
    success_url = '/communication_objects/'


class CommunicationObjectEditView(UpdateView):
    model = models.CommunicationObject
    form_class = forms.CommunicationObjectForm
    success_url = '/communication_objects/'


class CommunicationObjectDeleteView(DeleteView):
    model = models.CommunicationObject
    success_url = '/communication_objects/'


class FolderTaskView(ListView):
    template_name = 'kernel/folder_task/index.html'
    model = models.FolderTask
    context_object_name = 'folders'


class FolderTaskViewAPI(views.APIView):

    def get(self, request):
        qs = models.FolderTask.objects.filter(parent=None).all()
        serializer = serializers.FolderTaskSerializer(qs, many=True)

        return Response({
            'core': {
                'data': serializer.data
            }
        })


class Task(ListView):
    template_name = 'kernel/task/index.html'
    model = models.Task
    context_object_name = 'tasks'


class PersonIdentifierView(ListView):
    template_name = 'kernel/person_identifier/index.html'
    model = models.PersonIdentifier
    context_object_name = 'person_identifiers'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_obj'] = forms.PersonIdentifierForm
        return ctx


class PersonIdentifierViewAPI(mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    model = models.PersonIdentifier
    serializer_class = serializers.PersonIdentifierSerializer
    queryset = models.PersonIdentifier.objects.all()


class PersonIdentifierCreateView(CreateView):
    model = models.PersonIdentifier
    form_class = forms.PersonIdentifierForm
    success_url = '/person_identifiers/'


class PersonIdentifierEditView(UpdateView):
    model = models.PersonIdentifier
    form_class = forms.PersonIdentifierForm
    success_url = '/person_identifiers/'
