from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from my_app.models import Task

def home(request):
	"""
	Fonction principale de la to do list.
	On affiche les tâches via un render().
	Ces tâches sont triées par ordre croissant via un order_by().
	"""
	task = Task.objects.all().order_by('place')
	return render(request, "task.html", {"alltask":task})
