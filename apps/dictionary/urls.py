from django.urls import path
from django.contrib.auth.decorators import (
    permission_required,
)

from apps.dictionary import views

app_name = 'dictionary'
urlpatterns = [
    path(
        'organizations/',
        permission_required(
            'dictionary.menu_view_organization', login_url='/login/'
        )
        (views.OrganizationsView.as_view()),
        name='organizations'
    ),
    path(
        'organization_create/',
        permission_required('dictionary.add_organization', login_url='/login/')
        (views.organization_create),
        name='organization_create'
    )
]
