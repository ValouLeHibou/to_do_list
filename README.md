# to_do_list
todo list pour Vingt Cinq

Bonjour Étienne,
Ici je vais décrire les différentes étapes réalisées pour cet exercice

- Installation Python & Django sur Windows
- Mise en place et compréhension de l'environnement MVT
- Création d'une vue (my_app/views.py)
- Création d'une URL pour la vue : localhost:8000/my_app/accueil (to_do_list/urls.py & my_app/urls.py)
- Création d'un modèle Django (my_app/models.py) via une class Task relié à une table BDD nommée my_app_task (db.sqlite3)
- Création d'un Template HTML pour l'affichage (my_app/templates/task.html)

Avant de pouvoir commencer l'exercice, j'ai passé quelques heures sur les tutos pour pourvoir réaliser l'exercice, mes
connaissance en Django étant nul. ^^

Je me suis tout d'abord concentré sur les conventions de Django en m'efforcant de respecter la méthode MVT.
J'ai finalement réussi à créer une BDD, à remplir une table et à finalement l'afficher via la view en utilisant un template HTML.
J'ai malheureusement passé beaucoup trop de temps sur cette partie, m'handicapant pour la suite

J'ai donc réalisé (comme demandé) la Class Task avec une fonction que j'ai appelé order() contenant la logique de trie et
de déplacement des différentes taches dans la to do list. Ayant déjà dépassé le temps imparti je n'ai pas réussi
à relier ce morceau de code au reste du programme et à le rendre fonctionnel.

C'était en tout cas très intéressant. J'ai particulièrement aimé l'ORM de Djando très pratique. En revanche j'ai eu un peu de
mal sur la syntaxe générale, les nommages etc.
