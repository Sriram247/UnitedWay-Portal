from django.http import HttpResponse
from django.shortcuts import render
from backendApp.models import *
import json
from django.http import JsonResponse

import csv



def index(request):
    project_list = ProjectListNews.objects.all()
    
    context = {
        'projects': project_list,
    }
    
    return render(request,"backendApp/index.html",context)

def exportjson(request):
    # Fetch all HousingProject objects from the database
    projects = HousingProject.objects.all()
    
    # Prepare a list to hold project data
    project_data = []

    # Loop through each project and convert it to a dictionary
    for project in projects:
        project_data.append({
            "province": project.province,
            "project_phase": project.project_phase,
            "dwelling_type": project.dwelling_type,
            "housing_model": project.housing_model,
            "location": project.location,
            "number_of_units": project.number_of_units,
            "project_partner_type": project.project_partner_type,
            "partner_name": project.partner_name,
            "demographic": project.demographic,
            "x_coordinate": project.x_coordinate,
            "y_coordinate": project.y_coordinate,
        })
    
    # Convert the list of dictionaries to JSON format
    response_data = json.dumps(project_data)

    # Return the JSON response as a downloadable file
    return JsonResponse(response_data, safe=False, content_type='application/json')


def exportcsv(request):
    # Create the HttpResponse object with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="housing_projects.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Write the header row
    writer.writerow([
        'Province',
        'Project Phase',
        'Dwelling Type',
        'Housing Model',
        'Location',
        'Number of Units',
        'Project Partner Type',
        'Partner Name',
        'Demographic',
        'X Coordinate',
        'Y Coordinate'
    ])

    # Fetch all HousingProject objects from the database
    projects = HousingProject.objects.all()

    # Write each project data as a row in the CSV
    for project in projects:
        writer.writerow([
            project.province,
            project.project_phase,
            project.dwelling_type,
            project.housing_model,
            project.location,
            project.number_of_units,
            project.project_partner_type,
            project.partner_name,
            project.demographic,
            project.x_coordinate,
            project.y_coordinate,
        ])

    return response
