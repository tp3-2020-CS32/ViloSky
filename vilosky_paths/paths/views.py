from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from paths.forms import UserForm, UserProfileForm, SearchForm
from django.contrib.auth.decorators import login_required
from paths.models import Resource

# Create your views here.

def home(request):
	return render(request, 'paths/home.html')

def search(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        
        if search_form.is_valid():
            all_tag_details = (search_form.cleaned_data["personal_details_tags"] | search_form.cleaned_data["disability_tags"] | search_form.cleaned_data["current_work_situations"]
                                | search_form.cleaned_data["work_place_barriers_tags"] | search_form.cleaned_data["last_paid_work_tags"] | search_form.cleaned_data["industry_tags"]
                                | search_form.cleaned_data["area_of_interest_tags"] | search_form.cleaned_data["formal_qulifications_tags"] | search_form.cleaned_data["current_experience_tags"]
                                | search_form.cleaned_data["ideal_hours_tags"] | search_form.cleaned_data["goals_tags"] )
            print(all_tag_details)
            search_tags_list = []
            for tag in list(all_tag_details.values("tag_name")):
                search_tags_list.append(tag["tag_name"])
            request.session['search_tags'] = search_tags_list

            return redirect('/paths/dashboard')
        else:
            print(search_form.errors)
    else:
        search_form = SearchForm()

    return render(request, 'paths/search.html', context = {'search_form':search_form})
	
def dashboard(request):
    search_tags = request.session['search_tags']
    print((search_tags))
    resources = Resource.objects.filter(tags__tag_name__in= search_tags).distinct()
    resources_urls = [resource.url for resource in resources]

    return render(request, 'paths/dashboard.html', context = {'resources':resources_urls})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request, 'paths/register.html', context = {'user_form':user_form,
                                                            'profile_form':profile_form,
                                                            'registered':registered})
                                                            
                                                            
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('paths:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'paths/login.html')
        
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('paths:home'))