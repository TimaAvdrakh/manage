from django.urls import path, include
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)
from rest_framework import routers
from apps.kernel import views

router = routers.DefaultRouter()

app_name = 'kernel'
urlpatterns = [
    # path('api/', include(router.urls)),

    path(
        '',
        views.IndexView.as_view(),
        name='index'
    ),
    path(
        'folder_task/',
        views.FolderTaskView.as_view(),
        name='folder_task'
    ),
    path(
        'api/folder_task/',
        views.FolderTaskViewAPI.as_view(),
        name='folder_task_api'
    ),
    path(
        'tasks/',
        views.Task.as_view(),
        name='task_index'
    ),
    path(
        'communication_objects/',
        views.CommunicationObjectView.as_view(),
        name='communication_object_index'
    ),
    path(
        'api/communication_objects/<int:pk>/',
        views.CommunicationObjectViewAPI.as_view({'get': 'retrieve'})
    ),
    path(
        'communication_objects/create/',
        views.CommunicationObjectCreateView.as_view(),
        name='communication_object_create'
    ),
    path(
        'communication_objects/edit/<int:pk>/',
        views.CommunicationObjectEditView.as_view(),
        name='communication_object_edit'
    ),
    path(
        'communication_objects/delete/<int:pk>/',
        views.CommunicationObjectDeleteView.as_view(),
        name='communication_object_delete'
    ),
]
