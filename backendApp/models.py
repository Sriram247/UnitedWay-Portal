from django.db import models

class HousingProject(models.Model):
    PROVINCE_CHOICES = [
        ('NS', 'Nova Scotia'),
        ('NB', 'New Brunswick'),
        ('PEI', 'Prince Edward Island'),
    ]

    PROJECT_PHASE_CHOICES = [
        ('Planned', 'Planned'),
        ('Underway', 'Underway'),
        ('Complete', 'Complete'),
    ]

    DWELLING_TYPE_CHOICES = [
        ('Single Family Unit', 'Single Family Unit'),
        ('Tiny Home', 'Tiny Home'),
        ('Micro Shelter', 'Micro Shelter'),
    ]

    HOUSING_MODEL_CHOICES = [
        ('Co-operative', 'Co-operative'),
        ('Supportive Housing', 'Supportive Housing'),
        ('Other (Co-living)', 'Other (Co-living)'),
        ('Shelter', 'Shelter'),
    ]

    PROJECT_PARTNER_TYPE_CHOICES = [
        ('Developer', 'Developer'),
        ('Other Partner', 'Other Partner'),
        ('Charitable Partner', 'Charitable Partner'),
    ]

    province = models.CharField(max_length=3, choices=PROVINCE_CHOICES,null=True)
    project_phase = models.CharField(max_length=10, choices=PROJECT_PHASE_CHOICES,null=True)
    dwelling_type = models.CharField(max_length=20, choices=DWELLING_TYPE_CHOICES,null=True)
    housing_model = models.CharField(max_length=30, choices=HOUSING_MODEL_CHOICES,null=True)
    location = models.CharField(max_length=100,null=True)
    number_of_units = models.PositiveIntegerField(null=True)
    project_partner_type = models.CharField(max_length=20, choices=PROJECT_PARTNER_TYPE_CHOICES,null=True)
    partner_name = models.CharField(max_length=100,null=True)
    demographic = models.CharField(max_length=100,null=True)
    x_coordinate = models.FloatField(null=True)
    y_coordinate = models.FloatField(null=True)

    def __str__(self):
        return f"{self.location} - {self.demographic}"


class ProjectListNews(models.Model):
    title = models.CharField(max_length=255)  # Title of the project (required)
    summarize = models.TextField(null=True, blank=True)    
    link = models.CharField(max_length=255)   # Link to more information (required)
    location = models.CharField(max_length=255, null=True, blank=True)  # Location of the project (nullable)
    no_of_units = models.CharField(max_length=10, null=True, blank=True)  # Number of units (nullable)
    dwelling_type = models.CharField(max_length=100, null=True, blank=True)  # Type of dwelling (nullable)
    project_phase = models.CharField(max_length=50, null=True, blank=True)  # Current phase of the project (nullable)


    def __str__(self):
        return self.title  # String representation of the model
