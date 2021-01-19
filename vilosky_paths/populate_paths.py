import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vilosky_paths.settings')

import django
django.setup()
from paths.models import Tag, Resource

def populate():
    
    resources = [
        {'name' : 'Returning to office after Maternity leave',
        'tags' : ['Female','Maternity Leave']},
        ]
    
    for res in resources:
        add_resource(res['name'],res['tags'])
        

def add_resource(name,tag_list):
    new_resource = Resource.objects.get_or_create()
    new_resource.name = name
    for tag in tag_list:
        add_tag(new_resource,tag)
    new_resource.save()
    return new_resource
    

def add_tag(resource,tag_name):
    check_tag = Tag.objects.filter(tag_name=tag_name)
    if check_tag.exists():
        resource.tags.add(check_tag)
        resource.save()
        return resource
    else:
        new_tag = Tag.objects.get_or_create(tag_name=tag_name)
        new_tag.save()
        resource.tags.add(new_tag)
        resource.save()          
        return resource    