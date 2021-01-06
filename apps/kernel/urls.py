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

    ## folder_task
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
        'folder_task/create/',
        views.folder_task_create,
        name='folder_task_create'
    ),
    path(
        'folder_task/delete/<int:pk>/',
        views.FolderTaskDeleteView.as_view(),
        name='folder_task_delete'
    ),

    ## tasks
    path(
        'tasks/',
        views.Task.as_view(),
        name='task_index'
    ),

    ## communication_objects
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

    ## person_identifiers
    path(
        'person_identifiers/',
        views.PersonIdentifierView.as_view(),
        name='person_identifier_view'
    ),
    path(
        'api/person_identifiers/<int:pk>/',
        views.PersonIdentifierViewAPI.as_view({'get': 'retrieve'})
    ),
    path(
        'person_identifiers/create/',
        views.PersonIdentifierCreateView.as_view(),
        name='person_identifiers_create'
    ),
    path(
        'person_identifiers/edit/<int:pk>/',
        views.PersonIdentifierEditView.as_view(),
        name='person_identifiers_edit'
    ),
]
