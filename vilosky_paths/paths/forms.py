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
    selected_tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), to_field_name="tag_name")