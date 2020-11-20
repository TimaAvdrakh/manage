from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView

from apps.userapp.models import MainUser
from apps.userapp.forms import MainUserForm


class UserView(ListView):
    template_name = 'userapp/index.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        qs = MainUser.objects.filter(is_superuser=False).all()
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['add_form'] = MainUserForm
        return ctx


def add_user(request):
    if request.method == 'POST':
        form = MainUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/', status=200)
    return HttpResponse(status=400)
