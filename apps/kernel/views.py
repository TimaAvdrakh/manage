from django.views.generic import (
    TemplateView,
    ListView,
)


class IndexView(TemplateView):
    template_name = 'kernel/index.html'
