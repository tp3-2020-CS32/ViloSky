from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

"""
All the categories of tags used to label resources.
"""
class Tag(models.Model):
    Gender = "Gender"
    Sexual_Orientation = "Sexual orientation"
    Ethnicity = "Ethnicity"
    Disability = "Physical or mental disability"
    Current_Work_Situation = "Current work situation"
    Work_Place_Barriers = "Current workplace barriers"
    Last_Paid_Work = "Time since last paid work"
    Industry = "Industries interested in"
    Area_Of_Interest = "Area of interest"
    Formal_Qualifications = "Formal qualifications"
    Current_Experience = "Current experience"
    Ideal_Hours = "Ideal working hours a week"
    Goals = "Goals"

    tag_categories_choices = ((Gender, "Gender"),
                              (Sexual_Orientation, "Sexual orientation"),
                              (Ethnicity, "Ethnicity"),
                              (Disability, "Physical or mental disability"),
                              (Current_Work_Situation, "Current work situation"),
                              (Work_Place_Barriers, "Current workplace barriers"),
                              (Last_Paid_Work, "Time since last paid work"),
                              (Industry, "Industries interested in"),
                              (Area_Of_Interest, "Area of interest"),
                              (Formal_Qualifications, "Formal qualifications"),
                              (Current_Experience, "Current Experience"),
                              (Ideal_Hours, "Ideal working hours a week"),
                              (Goals, "Goals"))

    tag_name = models.CharField(max_length=50, unique=False)
    tag_categories = models.CharField(
        max_length=50, choices=tag_categories_choices, default=Gender)

    def __str__(self):
        return self.tag_name

"""
Creates an instance of a resource with a given name, media, url with relevant 
tags assigned to it. Can hold a file and/or a url for an external site.
"""
class Resource(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tags = models.ManyToManyField(Tag)
    media = models.FileField(upload_to='resources/', null=True, blank=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

"""
Stores the tags, time and current user in order to recreate previous searches.
"""
class SearchResults(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    tags_searched = models.ManyToManyField(Tag, blank=True)
    profile = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.time.strftime("%d/%m/%Y %I:%M %p"))


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username
