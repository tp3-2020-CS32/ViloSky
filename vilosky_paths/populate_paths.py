import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vilosky_paths.settings')

import django
django.setup()
from paths.models import Tag, Resource

def populate():
    
    print("Beginning population")
    resources = [
        {'name' : 'Returning to office after Maternity leave',
        'tags' : ['Female','Maternity Leave']},
        {'name' : 'Career Focus',
        'tags' :['Male','Female','Business']},
        ]
    
    for res in resources:
        add_resource(res['name'],res['tags'])
    
    print("Population script complete")
        

def add_resource(name,tag_list):

    check_res = Resource.objects.filter(name=name)
    if check_res.exists():   
        new_resource = check_res[0]
    else:
        new_resource = Resource.objects.get_or_create(name = name)[0]
        new_resource.save()       
    for tag in tag_list:
        add_tag(new_resource,tag)
    new_resource.save()
    return new_resource
    

def add_tag(resource,tag_name):
    check_tag = Tag.objects.filter(tag_name=tag_name)
    if check_tag.exists():
        resource.tags.add(check_tag[0])
        resource.save()
        return resource
    else:
        new_tag = Tag.objects.get_or_create(tag_name=tag_name)[0]
        new_tag.save()
        resource.tags.add(new_tag)
        resource.save()          
        return resource


#Main
if __name__ == '__main__':
	populate()