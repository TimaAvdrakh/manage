from django.http import HttpResponse, HttpResponseRedirect
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

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # ctx['form_obj'] = forms.FolderTaskForm
        return ctx


class FolderTaskViewAPI(views.APIView):

    def get(self, request):
        qs = models.FolderTask.objects.filter(parent=None).all()
        serializer = serializers.FolderTaskSerializer(qs, many=True)

        return Response({
            'core': {
                'data': serializer.data
            }
        })


class FolderTaskCreateView(CreateView):
    model = models.FolderTask
    form_class = forms.FolderTaskForm
    success_url = '/folder_task/'

    def form_valid(self, form):
        print('FORM: ', form)
        ft = form.save(commit=False)
        print(ft)
        return HttpResponseRedirect(self.get_success_url())


def folder_task_create(request):

    form = forms.FolderTaskForm(request.POST)

    if form.is_valid():
        obj = models.FolderTask.objects.create(
            name=form.cleaned_data.get('name'),
            parent_id=form.cleaned_data.get('parent'),
        )
        print(f'OBJ: {obj}')

    print('NO OU NOU VALID: ', form)
    return HttpResponse(status=200)


# Task

class Task(ListView):
    template_name = 'kernel/task/index.html'
    model = models.Task
    context_object_name = 'tasks'


# PersonIdentifier

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
