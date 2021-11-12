#from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
   # return HttpResponse("<h1>Bienvenue sur mon site</h1>")
   # Cette fois ci on veut retourner une templte à la place d'unbe chaine de caractères
   # dans la fct suivante on passe comme paramètre le chemin relative vers notre fichier html
   #return render(request, "index.html")
   #On ajoute le paramètre contexte ==> qui contient un dictionnaire avec des clés et des valeurs
   # ce dictionnaire va nous permet d'insérer des données à  notre page
   return render(request, "DocBlog/index.html", context={"date": datetime.today(),"prenom": "khaoula"})