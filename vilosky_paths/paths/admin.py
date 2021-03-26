from django.contrib import admin
from paths.models import UserProfile, Tag, Resource, SearchResults

admin.site.register(UserProfile)
admin.site.register(Tag)
admin.site.register(Resource)
admin.site.register(SearchResults)
