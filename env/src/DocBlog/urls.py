"""DocBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from .views import index
#from blog.views import index as blog_index

urlpatterns = [
    #Connecter une vue à un url :
    path('', index, name="index"),#c'est mieux de nommer les urls
    path('admin/', admin.site.urls),
    #Il faut inclure les urls de notre app de blog dans le projet django
    # Donc on va créer un nouveau fichier pour les urls de notre app
    path('blog/', include("blog.urls")),
    #path('blog/index/', blog_index) #On peut le faire directement dans le fichier 'urls.py' de l'applictaion
]
