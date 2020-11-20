from django.urls import path
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)

from apps.kernel import views

app_name = 'kernel'
urlpatterns = [
    path('', login_required(views.IndexView.as_view(), login_url='/login/')),
    path(
        'index',
        permission_required(
            'userapp.',
            login_url='/login/'
        )(views.TemplateView.as_view),
        name='index'
    ),
]
