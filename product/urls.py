from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import CreateProduct

urlpatterns = [
	
	url('^create/$',CreateProduct.as_view(),name='create'),
	url('^thanks/$',TemplateView.as_view(template_name='product/thanks.html')),
]