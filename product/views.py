from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from .forms import CreateProductForm
# Create your views here.

class CreateProduct(FormView):
	form_class 		= CreateProductForm
	template_name 	= 'product/createproduct.html'
	success_url		= '/product/thanks'

	def form_valid(self,form):
		form.save()
		return super().form_valid(form)