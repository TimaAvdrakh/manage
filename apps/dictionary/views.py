from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, FormView

from apps.dictionary.models import (
    Organization,
    ORG_KIND,
)
from apps.dictionary.forms import (
    OrganizationForm,
)


class OrganizationsView(ListView):
    template_name = 'dictionary/organization/index.html'
    model = Organization

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['org_kind'] = ORG_KIND
        ctx['add_form'] = OrganizationForm
        return ctx


def organization_create(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/organizations/', status=200)
        return HttpResponseRedirect(reverse('dictionary:organizations'))
    return HttpResponse(status=400)
