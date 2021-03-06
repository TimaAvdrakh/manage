from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from rest_framework import viewsets, mixins, views
from rest_framework.response import Response

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from apps.system.mixins import UserRequestMixin
from apps.kernel import (
    serializers,
    models,
    forms,
)
from apps.kernel.handlers import (
    communication_object,
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


class CommunicationObjectCreateView(UserRequestMixin, CreateView):
    model = models.CommunicationObject
    form_class = forms.CommunicationObjectForm
    success_url = '/communication_objects/'

    user_request_number = 'Запрос 1.А'
    class_name = communication_object.CreateCommunicationObjectHandler
    kind = 'simple'

    def description(self) -> str:
        return '''        ◦ Наименование органа, осуществляющего проведение ОРМ или надзор;
        ◦ права доступа;
        ◦ папка (папки) заданий;
        ◦ срок действия учетной записи;
        ◦ статус доступа.


'''


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


def folder_task_create(request):
    form = forms.FolderTaskForm(request.POST)

    if form.is_valid():
        obj = models.FolderTask.objects.create(
            name=form.cleaned_data.get('name'),
            parent_id=form.cleaned_data.get('parent'),
        )
        messages.success(
            request,
            message=f'Папка задания "{obj.name}" успешно создана!'
        )
        return redirect('/folder_task/')
    return HttpResponse(status=200)


class FolderTaskDeleteView(DeleteView):
    model = models.FolderTask
    success_url = '/folder_task/'

    def delete(self, request, *args, **kwargs):
        parents = models.FolderTask.objects.filter(
            parent_id=self.kwargs.get('pk')
        ).exists()
        if parents:
            messages.warning(
                request,
                f'Ошибка удаления папки: {self.kwargs.get("pk")}. У записи ' +
                f'существуют дочерние элементы'
            )
            return redirect(self.success_url)
        messages.info(
            request,
            extra_tags='success',
            message=f'Папка заданий {self.kwargs.get("pk")} успешно удалена.'
        )
        return super().delete(request, *args, **kwargs)


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
