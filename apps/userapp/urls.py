from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = 'userapp'
urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='userapp/auth/login.html'),
        name='login'
    ),
    path(
        'change_password/',
        login_required(
            auth_views.PasswordChangeView.as_view(
                template_name='userapp/auth/change_password.html',
                success_url='/password_change_done/',
            )
        ),
        name='change_password',
    ),
    path(
      'password_change_done/',
      login_required(auth_views.PasswordChangeDoneView.as_view(
          template_name='userapp/auth/password_change_done.html',
      )),
      name='password_change_done'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]
