from rest_framework import viewsets, mixins, views
from rest_framework.response import Response

from apps.kernel import (
    serializers,
    models,
)

from django.views.generic import (
    TemplateView,
    ListView,
)


class IndexView(TemplateView):
    template_name = 'kernel/index.html'


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

