from datetime import datetime, date
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
# Create your views here.
from django.urls import reverse

from core.utils import *
from django.contrib.auth import get_user_model
from structure.forms import *
from structure.models import District
from jsonview.decorators import json_view

def index(request):
    structureSantes = StructureSante.objects.all()
    return render(request, "structure/index.html", locals())


def create(request):
    form = StructureForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, "structure/form.html", locals())

@json_view
def save_structure(request):
    form = StructureForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return {'succes':True}
    ctx = {}
    ctx.update(csrf(request))
    form_html = render_crispy_form(form, context=ctx)
    return {'success': False, 'form_html': form_html}

def save_str(request):
    form = StructureForm(request.POST or None, request.FILES or None)
    data ={}
    if request.is_ajax():
        if form.is_valid():
            form.save()

            data = {
                'Class': "alert-success",
                'Message': "L'enregistrement s'est bien effectuer"
            }
            return JsonResponse(data)

        else:
            data = {
                'error': form.errors,
                'is_valid': False
            }
            return JsonResponse(data, status=400)

    else:
        context = {
            'form': form,
        }
        return render(request, 'structure/form.html', context)

def update(request, pk):
    structure = get_object_or_404(StructureSante, pk=pk)
    form = StructureForm(request.POST or None, request.FILES or None, instance=structure)
    if form.is_valid():
        form.save()
    return render(request, "structure/update.html", locals())


def detail(request, pk):
    structure_id = pk
    structure = get_object_or_404(StructureSante, pk=pk)
    agents = AgentStructure.objects.filter(structureSante__pk=pk)
    professionels = ProfessionelSante.objects.filter(StructureSante__pk=pk)
    return render(request, "structure/detail.html", locals())


def desactivate(request):
    if request.POST:
        structure = get_object_or_404(StructureSante, pk=request.POST.get("pk"))
        is_active = request.POST.get("is_active")
        statut = False if is_active == "True" else True  # desactive si il est deja activé et vise versa
        structure.is_active = statut
        structure.save()
        return redirect("structure.index")
    else:
        raise Http404


def ajouter_agent(request, structure_id):
    form = PersonelForm(request.POST or None, request.FILES or None)
    agentform = AgentStructureForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        login = generateLogin(first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'))
        User = get_user_model()
        user = User.objects.create_user(
            username=login,
            password=generatePwd(),
            email=request.POST.get('email'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            birthday=datetime.strptime(request.POST.get('birthday'), "%d/%m/%Y").strftime("%Y-%m-%d"),
            sexe=request.POST.get('sexe'),
            phone=request.POST.get('phone'),
            adresse=request.POST.get('adresse'),
        )
        user.save()

        agentStructure = AgentStructure.objects.create(
            numeroAgent=request.POST.get('numeroAgent'),
            structureSante=StructureSante.objects.get(pk=structure_id),
            user=user,
        )
        agentStructure.save()
        messages.success(request, "L'agent  " + login + " a été ajoutée avec Success")
        return redirect(reverse('structure.detail', kwargs={"structure_id": structure_id}))
    return render(request, "structure/agents/form.html", locals())


def search_professionel_sante(request, structure_id):
    form = SearchPsForm(request.POST or None, request.FILES or None)

    if request.POST:
        matricule = request.POST.get("matricule")
        num_ordre = request.POST.get("matricule")
        tel = request.POST.get("matricule")
        if not matricule and  not num_ordre and  not tel :
            return redirect(reverse('structure.ajout_professionel_sante', kwargs={"structure_id": structure_id}))

        if form.is_valid():
            ps = ProfessionelSante.objects
            if  matricule:

                ps.filter(matricule = matricule)
            if  num_ordre:
                ps.filter(numOrdre = num_ordre)
            if  tel:
                ps.filter(user__phone = tel)
            ps.get()
            if not ps :
                return redirect(reverse('structure.ajout_professionel_sante', kwargs={"structure_id": structure_id}))
            else :
                return redirect(reverse('structure.ajout_professionel_sante', kwargs={"structure_id": structure_id,"ps":ps.id}))

    return render(request, "structure/ps/search.html", locals())


def ajout_professionel_sante(request, structure_id, ps=None):
    if not ps :
        form = PersonelForm(request.POST or None, request.FILES or None)
        psform = ProfessionelSanteForm(request.POST or None, request.FILES or None)
    else :
        form = PersonelForm(request.POST or None, request.FILES or None)
        psform = ProfessionelSanteForm(request.POST or None, request.FILES or None)

    if request.POST:
        if form.is_valid():
            login = generateLogin(first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'))
            User = get_user_model()
            user = User.objects.create_user(
                username=login,
                password=generatePwd(),
                email=request.POST.get('email'),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                birthday=datetime.strptime(request.POST.get('birthday'), "%d/%m/%Y").strftime("%Y-%m-%d"),
                sexe=request.POST.get('sexe'),
                phone=request.POST.get('phone'),
                adresse=request.POST.get('adresse'),
            )
            user.save()

            professionelSante = ProfessionelSante.objects.create(
                matricule=request.POST.get('matricule'),
                numOrdre=request.POST.get('numOrdre'),
                categorie=CategoriePs.objects.get(pk=request.POST.get('categorie')),
                qualite=QualitePs.objects.get(pk=request.POST.get('qualite')),
                specialite=SpecialitePs.objects.get(pk=request.POST.get('specialite')),
                user=user,
            )
            professionelSante.save()
            messages.success(request, "L'agent  " + login + " a été ajoutée avec Success")
            return redirect(reverse('structure.detail', kwargs={"structure_id": structure_id}))

    return render(request, "structure/ps/form.html", locals())
