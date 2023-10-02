from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def protected_page(request, path):
    return render(request, path)

class IndexPageView(LoginRequiredMixin, TemplateView):
    # template_name = 'main/index.html'
    pass

class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
