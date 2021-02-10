from django.test import TestCase
from paths.models import *

class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(tag_name='Maternity leave', tag_categories='Current_Work_Situation')
    
    def test_tag_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('tag_name').verbose_name
        self.assertEqual("tag name", field_label)
    
    def test_tag_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('tag_name').max_length
        self.assertEqual(max_length,50)
    
    def test_tag_categories_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('tag_categories').max_length
        self.assertEqual(max_length, 50)
    
    def test_object_name_is_tag_name(self):
        tag = Tag.objects.get(id=1)
        expected_object_name = tag.tag_name
        self.assertEqual(expected_object_name, str(tag))

class ResourceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(tag_name='Maternity leave', tag_categories='Current_Work_Situation')
        Resource.objects.create(url='https://www.euraxess.sk/en/main/info/working/employment/maternity-leave-family-care', name="Maternity leave")
        resource = Resource.objects.get(id=1)
        resource.tags.add(Tag.objects.get(id=1))
        
    def test_resource_name_label(self):
        resource = Resource.objects.get(id=1)
        field_label = resource._meta.get_field('name').verbose_name
        self.assertEqual("name", field_label)
        
    def test_resource_name_max_length(self):
        resource = Resource.objects.get(id=1)
        max_length = resource._meta.get_field('name').max_length
        self.assertEqual(max_length,50)
    
    def test_object_name_is_reource_name(self):
        resource = Resource.objects.get(id=1)
        expected_object_name = resource.name
        self.assertEqual(expected_object_name, str(resource))