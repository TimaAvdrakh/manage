from django.urls import path
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)

from apps.kernel import views

app_name = 'kernel'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path(
        'index',
        permission_required(
            'userapp.',
            login_url='/login/'
        )(views.TemplateView.as_view),
        name='index'
    ),
    path(
      'organizations',

    ),
]
