from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_list_or_404, get_object_or_404, render_to_response
from django.http import HttpResponse
from artiste.models import Artiste, Oeuvre
from django.views.generic.base import TemplateView
from django import template

# Create your views here.

class ArtistList(ListView):
	
	template_name = "liste-artiste.html"
	model = Artiste

	def get_context_data(self, **kwargs):
		context = super(ArtistList, self).get_context_data(**kwargs)
		# Permet de retourner tous les objets du model Oeuvre
		context['oeuvres'] = Oeuvre.objects.all()

		return context

class ArtworkList(ListView):
	
	template_name = "liste-oeuvre.html"
	model = Oeuvre

	def get_context_data(self, **kwargs):
		context = super(ArtworkList, self).get_context_data(**kwargs)
		# Permet de retourner tous les objets du model Artiste
		context['artiste'] = Artiste.objects.all()

		return context

#class OeuvreDetail(DetailView):
	
	#template_name = "oeuvres_detailV1.html"
	#model = Oeuvre

	#def get_context_data(self, **kwargs):
		#context = super(OeuvreDetail, self).get_context_data(**kwargs)
		# Permet de retourner tous les objets du model Artiste
		#context['artiste'] = Artiste.objects.all()

		#return context

class ArtistDetail(DetailView):
	
	template_name = "page-artiste.html"
	model = Artiste

	def get_context_data(self, **kwargs):
		context = super(ArtistDetail, self).get_context_data(**kwargs)
		# Permet de retourner tous les objets du model Oeuvre
		context['oeuvres'] = Oeuvre.objects.all()

		return context
