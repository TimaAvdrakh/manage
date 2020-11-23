from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django_filters.views import FilterView

from apps.userapp.models import MainUser
from apps.userapp.forms import MainUserForm
from apps.userapp.filters import MainUserFilter


# class UserView(ListView):
#     template_name = 'userapp/index.html'
#     context_object_name = 'accounts'
#     queryset = MainUser.objects.filter(is_superuser=False).all()
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         ctx['add_form'] = MainUserForm
#         return ctx


class UserView(FilterView):
    model = MainUser
    context_object_name = 'accounts'
    template_name = 'userapp/index.html'
    filterset_class = MainUserFilter


def add_user(request):
    if request.method == 'POST':
        form = MainUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/', status=200)
    return HttpResponse(status=400)
