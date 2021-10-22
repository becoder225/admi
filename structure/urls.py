"""admi URL Configuration

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


from django.urls import path
from structure import views

urlpatterns = [
    path('', views.index, name='structure.index'),
    path('add/', views.create, name='structure.create'),
    path('save/', views.save_str, name='structure.save_structure'),
    path('<int:pk>/edit', views.update, name='structure.update'),
    path('<int:pk>/detail', views.detail, name='structure.detail'),
    path('desactivate', views.desactivate, name='structure.desactivate'),
    path('agent/<int:structure_id>/add', views.ajouter_agent, name='structure.ajouter_agent'),
    path('ps/<int:structure_id>/add', views.ajout_professionel_sante, name='structure.ajout_professionel_sante'),
    path('ps/<int:structure_id>/add/<int:ps>', views.ajout_professionel_sante, name='structure.ajout_professionel_sante'),
    path('ps/<int:structure_id>/search', views.search_professionel_sante, name='structure.search_professionel_sante'),

]
