
from django.db import models
from core.models import *

# Create your models here.


class District(models.Model):
    label = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("District")
        verbose_name_plural = ("Districts")

    def __str__(self):
        return self.label


class Region(models.Model):
    label = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Region")
        verbose_name_plural = ("Regions")

    def __str__(self):
        return self.label


class Departement(models.Model):
    label = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Departement")
        verbose_name_plural = ("Departements")

    def __str__(self):
        return self.label


class SousPrefecture(models.Model):
    label = models.CharField(max_length=50)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Sous-Prefecture")
        verbose_name_plural = ("Sous-Prefectures")

    def __str__(self):
        return self.label


class Localite(models.Model):
    label = models.CharField(max_length=50)
    sousPrefecture = models.ForeignKey(SousPrefecture, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Localité")
        verbose_name_plural = ("Localités")

    def __str__(self):
        return self.label


class StatutJuridique(models.Model):
    label = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Statut Juridique")
        verbose_name_plural = ("Statut Juridiques")

    def __str__(self):
        return self.label


class Structure(models.Model):
    name = models.CharField(max_length=255, )
    adresse = models.CharField(max_length=255)
    adresse_geo = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=50, )
    telephone2 = models.CharField(max_length=50, null=True, blank=True)
    telephone3 = models.CharField(max_length=50, null=True, blank=True)
    fax = models.CharField(max_length=50, null=True, blank=True)
    code_four = models.CharField(max_length=50, null=True, blank=True)
    localisation_gps = models.CharField(max_length=50, null=True, blank=True)
    name_responsable = models.CharField(max_length=255, verbose_name=("Nom du responsable"))
    email_responsable = models.EmailField(max_length=255, null=True, blank=True)
    tel_reponsable = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    logo = models.ImageField(("Logo "), upload_to="static/MEDIA", height_field=None,
                             width_field=None, blank=True, null=True,
                             max_length=300)
    localite = models.ForeignKey(Localite, verbose_name=("localite"), on_delete=models.CASCADE)
    statutJuridique = models.ForeignKey(StatutJuridique, verbose_name=("Statut Juridique"), on_delete=models.CASCADE)
    description = models.TextField(verbose_name=("Infos. complémentaires"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = ("Prestataire")
        verbose_name_plural = ("Prestataires")

    def __str__(self):
        return self.name


class CategoriePs(models.Model):
    label = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Categorie Professionel de Santé")
        verbose_name_plural = ("Categories Professionel de Santé")

    def __str__(self):
        return self.label


class QualitePs(models.Model):
    label = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Qualite Professionel de Santé")
        verbose_name_plural = ("Qualites Professionel de Santé")

    def __str__(self):
        return self.label


class SpecialitePs(models.Model):
    label = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Specialite Professionel de Santé")
        verbose_name_plural = ("Specialites Professionel de Santé")

    def __str__(self):
        return self.label


class TypeStructureSante(models.Model):
    label = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Type  Structure de Santé")
        verbose_name_plural = ("Type  Structure de Santé")

    def __str__(self):
        return self.label


class Secteur(models.Model):
    label = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    typeStructureSante = models.ManyToManyField(TypeStructureSante)

    class Meta:
        verbose_name = ("Secteur  Structure de Santé")
        verbose_name_plural = ("Secteur  Structure de Santé")

    def __str__(self):
        return self.label


class StructureSante(Structure):
    numImmatriculation = models.CharField(max_length=255)
    typestructureSante = models.ForeignKey(TypeStructureSante,verbose_name=("Type"), on_delete=models.CASCADE, null=True, blank=True)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    structureParent = models.ForeignKey('self', null=True, blank=True, related_name='structureEnfant',
                                        on_delete=models.CASCADE)
    enAccorPrealable = models.BooleanField(default=False)

    class Meta:
        # abstract = True
        verbose_name = ("Structure de Stanté")
        verbose_name_plural = ("Structures de Stanté")

    def __str__(self):
        return self.numImmatriculation


class AgentStructure(models.Model):
    structureSante = models.ForeignKey(StructureSante, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numeroAgent = models.CharField(max_length=50,verbose_name=("N° Agent"),null=True, blank=False )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # abstract = True
        verbose_name = ("Agent des Structure de Stanté")
        verbose_name_plural = ("Agents desStructures de Stanté")

    def __str__(self):
        return self.numeroAgent


class ProfessionelSante(models.Model):
    categorie = models.ForeignKey(CategoriePs, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualite = models.ForeignKey(QualitePs, on_delete=models.CASCADE)
    specialite = models.ForeignKey(SpecialitePs, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=255, null=True, blank=True)
    numOrdre = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    StructureSante = models.ManyToManyField(StructureSante)

    class Meta:
        verbose_name = ("Professionel de Santé")
        verbose_name_plural = ("Professionels de Santé")

    def __str__(self):
        return self.categorie


class StructurePhanrmacie(Structure):
    numImmatriculation = models.CharField(max_length=255)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    enAccorPrealable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # abstract = True
        verbose_name = ("Structure de Stanté")
        verbose_name_plural = ("Structures de Stanté")

    def __str__(self):
        return self.numImmatriculation