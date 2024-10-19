from backendApp.models import HousingProject,ProjectListNews
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models with the custom admin class

admin.site.site_header = "United Way Portal"
admin.site.site_title = "Team Zenith"
admin.site.index_title = "United way - Stronger Locally. Stronger Together."


class HousingProjectResource(resources.ModelResource):

    class Meta:
        model = HousingProject
        
        fields = (
            'id','province', 'project_phase', 'dwelling_type', 'housing_model',
            'location', 'number_of_units', 'project_partner_type', 
            'partner_name', 'demographic', 'x_coordinate', 'y_coordinate'
        )


@admin.register(HousingProject)
class HousingProjectAdmin(ImportExportModelAdmin):
    resource_class = HousingProjectResource
    list_display = (
        'province', 'project_phase', 'dwelling_type', 'housing_model', 
        'location', 'number_of_units', 'project_partner_type', 
        'partner_name', 'demographic', 'x_coordinate', 'y_coordinate'
    )
    search_fields = ('province', 'location', 'partner_name', 'demographic')
    list_filter = ('province', 'project_phase', 'dwelling_type', 'housing_model', 'project_partner_type')


admin.site.register(ProjectListNews)