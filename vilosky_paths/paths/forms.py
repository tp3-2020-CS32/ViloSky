from django import forms
from django.contrib.auth.models import User
from paths.models import UserProfile, Tag

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name',)

class SearchForm(forms.Form):
    personal_details_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Personal Details"), to_field_name="tag_name", required=False)
    disability_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Mental or Physical Disability"), to_field_name="tag_name", required=False)
    current_work_situations = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Current Work Situation"), to_field_name="tag_name", required=False)
    work_place_barriers_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Work Place Barriers"), to_field_name="tag_name", required=False)
    last_paid_work_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Time since last paid work"), to_field_name="tag_name", required=False)
    industry_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Industry"), to_field_name="tag_name", required=False)
    area_of_interest_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Area of Interest"), to_field_name="tag_name", required=False)
    formal_qulifications_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Formal Qualifications"), to_field_name="tag_name", required=False)
    current_experience_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Current Experience"), to_field_name="tag_name", required=False)
    ideal_hours_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Ideal Working Hours a Week"), to_field_name="tag_name", required=False)
    goals_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.filter(tag_categories="Goals"), to_field_name="tag_name", required=False)