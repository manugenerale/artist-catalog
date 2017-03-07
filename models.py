from __future__ import unicode_literals

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Artiste(models.Model):
	nom_artiste = models.CharField(_(u"Nom "), max_length=30)
	prenom_artiste = models.CharField(_(u"Prenom  "), max_length=30)
	description = models.CharField(_(u"Description  "), max_length=310)
	biographie = models.CharField(_(u"Biographie  "), max_length=1000)
	caracteristiques = models.CharField(_(u"Caracteristiques  "), max_length=400)
	url_image = models.ImageField(upload_to = "artiste/static/img/")	

	def __unicode__(self):
		return self.nom_artiste

	class Meta:
		app_label = "artiste"

class Oeuvre(models.Model):
	titre = models.CharField(_(u"Titre "), max_length=30)
	description = models.CharField(_(u"Description  "), max_length=400)
	url_oeuvre = models.ImageField(upload_to = 'artiste/static/img/')
	artiste = models.ForeignKey(Artiste)
	dimension = models.CharField(_(u"Dimension (a x b) "), max_length=30)
	type_oeuvre = models.CharField(_(u"Type oeuvre(peinture, photo,etc) "), max_length=30)
	date = models.CharField(_(u"Date "), max_length=30)

	def __unicode__(self):
		return self.titre

	class Meta:
		app_label = "artiste"


