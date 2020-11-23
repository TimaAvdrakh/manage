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
        'index',
        permission_required(
            'userapp.',
            login_url='/login/'
        )(views.TemplateView.as_view),
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
]
