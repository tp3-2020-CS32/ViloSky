from django import forms
from django.contrib.auth.models import User
from paths.models import UserProfile, Tag, Resource
from paths.models import UserProfile, Tag, SearchResults

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        
class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name',)

class SearchForm(forms.Form):
    gender_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Gender"), to_field_name="tag_name", required=False)
    sexual_orientation_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Sexual orientation"), to_field_name="tag_name", required=False)
    ethnicity_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Ethnicity"), to_field_name="tag_name", required=False)
    disability_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Physical or mental disability"), to_field_name="tag_name", required=False)
    current_work_situation_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Current work situation"), to_field_name="tag_name", required=False)
    work_place_barriers_tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.filter(tag_categories="Current workplace barriers"), to_field_name="tag_name", required=False)
    last_paid_work_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Time since last paid work"), to_field_name="tag_name", required=False)
    industry_tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.filter(tag_categories="Industries interested in"), to_field_name="tag_name", required=False)
    area_of_interest_tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.filter(tag_categories="Area of interest"), to_field_name="tag_name", required=False)
    formal_qualifications_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Formal qualifications"), to_field_name="tag_name", required=False)
    current_experience_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Current experience"), to_field_name="tag_name", required=False)
    ideal_hours_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Ideal working hours a week"), to_field_name="tag_name", required=False)
    goals_tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.filter(tag_categories="Goals"), to_field_name="tag_name", required=False)

class UploadResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('name', 'tags', 'media', 'url')
        widgets = {'media': forms.FileInput(), }
    
class PrevSearches(forms.Form):

   prev_searches = forms.ModelChoiceField(queryset = None, widget=forms.Select(attrs={'size':'10','class':'form-control prev-searches','required':''}), label="", empty_label=None)
   
   def __init__(self,user=None,*args, **kwargs):
        super(PrevSearches,self).__init__(**kwargs)
        if user:
            self.fields['prev_searches'].queryset = (SearchResults.objects.filter(profile=user)).order_by('time').reverse()
        
    
