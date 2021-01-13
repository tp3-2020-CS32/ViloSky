from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Tag(models.Model):
	tag_name = models.CharField(max_length = 50, unique=True)
	resources = models.ManyToManyField(Resource)
	
	def __str__(self):
        return self.tag_name
	
class Resource(models.Model):
	url = models.URLField(unique=True)
	name = models.CharField(max_length = 50, unique=True)
	tags = models.ManyToManyField(Tag)
	searches = models.ManyToManyField(SearchResults)
	
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
