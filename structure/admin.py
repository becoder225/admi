from django.contrib import admin
from structure.models import *
# Register your models here.
@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('label', 'region')
    list_filter = ('region', 'label')
    search_fields = ('label',)

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('label', 'district')
    list_filter = ('district', 'label')
    search_fields = ('label',)

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('label',)
    list_filter = ( 'label',)
    search_fields = ('label',)

@admin.register(SousPrefecture)
class SousPrefectureAdmin(admin.ModelAdmin):
    pass
@admin.register(Localite)
class LocaliteAdmin(admin.ModelAdmin):
    pass

@admin.register(StatutJuridique)
class StatutJuridiqueAdmin(admin.ModelAdmin):
    pass

@admin.register(TypeStructureSante)
class TypeStructureSanteAdmin(admin.ModelAdmin):
    pass
@admin.register(Secteur)
class SecteurAdmin(admin.ModelAdmin):
    pass

@admin.register(AgentStructure)
class AgentStructureAdmin(admin.ModelAdmin):
    pass

@admin.register(CategoriePs)
class CategoriePsAdmin(admin.ModelAdmin):
    list_display = ('label',)
    list_filter = ('label',)
    search_fields = ('label',)

@admin.register(QualitePs)
class QualitePsAdmin(admin.ModelAdmin):
    list_display = ('label',)
    list_filter = ('label',)
    search_fields = ('label',)

@admin.register(SpecialitePs)
class SpecialitePsAdmin(admin.ModelAdmin):
    list_display = ('label',)
    list_filter = ('label',)
    search_fields = ('label',)


@admin.register(ProfessionelSante)
class ProfessionelSanteAdmin(admin.ModelAdmin):
    list_display = ('matricule','numOrdre','specialite','qualite','categorie',)
    list_filter = ('matricule','specialite',)
    search_fields = ('matricule','specialite','numOrdre',)


@admin.register(StructureSante)
class StructureSanteAdmin(admin.ModelAdmin):
    pass