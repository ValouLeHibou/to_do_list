from django.db import models

class Task(models.Model):
	"""
	Classe définissant une liste
	que l'on peut potentiellement lire, modifier, effacer ou éditer.
	"""
	place = models.IntegerField()
	descr = models.CharField(max_length=100, default='default')

	def order(self, old_place, new_place):
		"""
		Gestion de l'ordre des taches
		L'utilisateur demande à modifier l'emplacement de la tâche.
		Par exemple la tâche 3 sera remonté en première position
		l'utilisateur va donc inscrire le nouvel emplacement en face de celle-ci,

		1- tache une <--.
		2- tache deux	|
		3- tache trois _| 1
		4- tache quatre
		._________.
		| VALIDER |
		'---------'
		Le bouton VALIDER retourne les variables : old_place & new_place
		respectivement égale à 3 et 1,
		représentant donc l'ancienne et la nouvelle valeur de l'emplacement
		"""

		if old_place > new_place:
			# Le nouvel emplacement est donc plus haut dans la liste
			all = Task.objects.all().order_by('place')
			for task in all:
				if task.order == old_place:
					# Si task.order est égale à l'ancienne place,
					# cela veux dire que nous sommes sur la tâche à déplacer :
					task.order = new_place
					return true
				task.order = task.order + 1
				# on augmente la valeur d'une tache et on la fait donc baisser dans la liste
		if old_place < new_place:
			all = Task.objects.all().order_by('place')
			# "-" pour inverser l'ordre pour faire la même chose que précédement mais dans l'autre sens
			# Le nouvel emplacement est donc plus bas dans la liste
			for task in all:
				if task.order == old_place:
					# même chose ici
					task.order = new_place
					return true
				task.order = task.order - 1
				# on baisse la valeur d'une tache et on la fait donc monter dans la liste
		if old_place == new_place:
			return true
