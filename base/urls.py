
from django.views.generic import  TemplateView
from django.urls import path,include, re_path

urlpatterns = [
   path('apexx/', include('djoser.urls')),
   path('apexx/', include('djoser.urls.jwt')),
]

urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'))
]

