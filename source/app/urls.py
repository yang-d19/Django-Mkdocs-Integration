from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from main.views import IndexPageView, ChangeLanguageView
from django.views.generic import TemplateView
# from main.views import protected_page

import os

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name = 'main/index.html'), name='index'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('accounts/', include('accounts.urls')),

    # path('homepage/friendlink/', TemplateView.as_view(template_name = 'main/homepage/friendlink/index.html')),
    # path('homepage/about/', TemplateView.as_view(template_name = 'main/homepage/about/index.html')),
    # path('homepage/qa/', TemplateView.as_view(template_name = 'main/homepage/qa/index.html')),

    # path('other_departments/about/', TemplateView.as_view(template_name = "main/other_departments/about/index.html")),
    # path('da/2019/23fall/CX/', IndexPageView.as_view(template_name = "main/da/2019/23fall/CX/index.html")),
    # path('da/2019/23fall/Empath/', IndexPageView.as_view(template_name = "main/da/2019/23fall/Empath/index.html")),
    # path('da/2019/23fall/Helin/', IndexPageView.as_view(template_name = "main/da/2019/23fall/Helin/index.html")),
    # path('da/2019/23fall/Orakel/', IndexPageView.as_view(template_name = "main/da/2019/23fall/Orakel/index.html")),
    # path('da/2019/23fall/QQ/', IndexPageView.as_view(template_name = "main/da/2019/23fall/QQ/index.html")),
    # path('da/2019/23fall/Qihang/', IndexPageView.as_view(template_name = "main/da/2019/23fall/Qihang/index.html")),
    # path('da/2019/23fall/Rain/', IndexPageView.as_view(template_name = "main/da/2019/23fall/Rain/index.html")),
    # path('da/2019/23fall/Venom/', IndexPageView.as_view(template_name = "main/da/2019/23fall/Venom/index.html")),
    # path('da/2019/23fall/Yuxiang/', IndexPageView.as_view(template_name = "main/da/2019/23fall/Yuxiang/index.html")),
    # path('da/2019/23fall/Zibu/', IndexPageView.as_view(template_name = "main/da/2019/23fall/Zibu/index.html")),
    # path('da/2019/23fall/summary/', IndexPageView.as_view(template_name = "main/da/2019/23fall/summary/index.html")),
    # path('da/2019/23fall/wkw/', IndexPageView.as_view(template_name = "main/da/2019/23fall/wkw/index.html")),
    # path('da/2019/23fall/zhiyuan/', IndexPageView.as_view(template_name = "main/da/2019/23fall/zhiyuan/index.html")),

    # path('da/2019/23fall/DingYang/DingYang/', IndexPageView.as_view(template_name = "main/da/2019/23fall/DingYang/DingYang/index.html")),
    # path('da/2019/23fall/Wenze/Wenze/', IndexPageView.as_view(template_name = "main/da/2019/23fall/Wenze/Wenze/index.html")),

    # path('da/2019/23fall/yyx/yyx/', IndexPageView.as_view(template_name = "main/da/2019/23fall/yyx/yyx/index.html")),

    # path('da/2019/exam_for_postgraduate/about/', TemplateView.as_view(template_name = "main/da/2019/exam_for_postgraduate/about/index.html")),
    # path('da/2019/postgraduate_recommendation/about/', TemplateView.as_view(template_name = "main/da/2019/postgraduate_recommendation/about/index.html")),
    # path('da/2019/work/about/', TemplateView.as_view(template_name = "main/da/2019/work/about/index.html")),

    # path('da/about/', TemplateView.as_view(template_name = "main/da/about/index.html")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


directory = "/home/ubuntu/dagrad-site/source/content/templates/main"  # Replace with the actual directory path

can_publish_prefix = ["homepage", "other_departments/about", "da/2019/exam_for_postgraduate/about",
                      "da/2019/postgraduate_recommendation/about", "da/2019/work/about",
                      "da/about/"]

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            # print(relative_path)
            url_path = relative_path.rsplit('/', 1)[0] + '/'
            template_name = 'main/' + relative_path

            isAdded = False
            for prefix in can_publish_prefix:
                if relative_path.startswith(prefix):
                    urlpatterns.append(path(url_path, TemplateView.as_view(template_name=template_name)))
                    isAdded = True
                    break
            if not isAdded:
                urlpatterns.append(path(url_path, IndexPageView.as_view(template_name=template_name)))

