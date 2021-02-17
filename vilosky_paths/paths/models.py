from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Tag(models.Model):
    
    #Below is all Categories of tags that get added to choices field
    Personal_Details = "Personal Details"
    Disability = "Mental or Physical Disability"
    Current_Work_Situation = "Current Work Situation"
    Work_Place_Barriers = "Work Place Barriers"
    Last_Paid_Work = "Time since last paid work"
    Industry = "Industry"
    Area_Of_Interest = "Area of Interest"
    Formal_Qualifications = "Formal Qualifications"
    Current_Experience = "Current Experience"
    Ideal_Hours = "Ideal Working Hours a Week"
    Goals = "Goals"
    
    tag_categories_choices = ( (Personal_Details, "Personal Details"),
                                (Disability, "Mental or Physical Disability"),
                                (Current_Work_Situation, "Current Work Situation"),
                                (Work_Place_Barriers, "Work Place Barriers"),
                                (Last_Paid_Work, "Time since last paid work"),
                                (Industry, "Industry"),
                                (Area_Of_Interest, "Area of Interest"),
                                (Formal_Qualifications, "Formal Qualifications"),
                                (Current_Experience, "Current Experience"),
                                (Ideal_Hours, "Ideal Working Hours a Week"),
                                (Goals, "Goals"))
    
    tag_name = models.CharField(max_length = 50, unique=True)    
    tag_categories = models.CharField(max_length = 50, choices=tag_categories_choices,default=Personal_Details)
    
    def __str__(self):
        return self.tag_name
	
class Resource(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    tags = models.ManyToManyField(Tag)
    media = models.FileField(upload_to='resources/', null=True)
    # url for if resource links to external media
    url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name
	
# currently only holds data on the search results, but could theoretically also
# hold the search inputs for users' future reference
class SearchResults(models.Model):
	time = models.DateTimeField(auto_now_add=True)  # should add the time a search was made automatically
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	resources = models.ManyToManyField(Resource)
	
	# unsure whether this will read well
	def __str__(self):
		return self.username + "'s search on " + self.time

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.user.username
