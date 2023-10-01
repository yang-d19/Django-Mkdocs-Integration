from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexPageView(LoginRequiredMixin, TemplateView):
    # template_name = 'main/index.html'
    pass

class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
