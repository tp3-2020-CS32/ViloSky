from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from paths.forms import UserForm, UserProfileForm, SearchForm, PrevSearches
from django.contrib.auth.decorators import login_required
from paths.models import Resource, UserProfile, SearchResults
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request, 'paths/home.html')

def search(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        
        if search_form.is_valid():
            all_tag_details = (search_form.cleaned_data["gender_tags"] | search_form.cleaned_data["sexual_orientation_tags"] | search_form.cleaned_data["ethnicity_tags"]
                                | search_form.cleaned_data["disability_tags"] | search_form.cleaned_data["current_work_situation_tags"] | search_form.cleaned_data["work_place_barriers_tags"]
                                | search_form.cleaned_data["last_paid_work_tags"] | search_form.cleaned_data["industry_tags"] | search_form.cleaned_data["area_of_interest_tags"]
                                | search_form.cleaned_data["formal_qualifications_tags"] | search_form.cleaned_data["current_experience_tags"] | search_form.cleaned_data["ideal_hours_tags"] 
                                | search_form.cleaned_data["goals_tags"] )
            print(all_tag_details)
            search_tags_list = []
            
            # adds search data to profile if logged in
            if request.user.is_authenticated:

                profile = request.user
                new = SearchResults(profile=profile)               
                new.save()
                
                for tag in list(all_tag_details.values("id")):
                    new.tags_searched.add(tag['id'])
                
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
    try:
        if request.session['just_registered']:
            messages.success(request, 'Thank you for registering, and welcome to Vilo Sky Paths!')
            request.session['just_registered'] = False
    except:
        pass
    try:
        search_tags = request.session['search_tags']
        print((search_tags))
        resources = Resource.objects.filter(tags__tag_name__in= search_tags).distinct()
    except:
        return render(request, 'paths/dashboard.html', context = None)

    return render(request, 'paths/dashboard.html', context = {'resources':resources})

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('paths:home'))
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            profile = profile_form.save(commit=False)
            user.first_name = profile.first_name
            user.last_name = profile.last_name
            user.save()
            profile.user = user
            profile.save()
            registered = True
            request.session['just_registered'] = True
            new_user = authenticate(username=user.username, password=user.password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse('paths:dashboard'))
        else:
            for error in user_form.errors:
                messages.error(request, str(user_form.errors[error]))
            for error in profile_form.errors:
                messages.error(request, str(profile_form.errors[error]))
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request, 'paths/register.html', context = {'user_form':user_form,
                                                            'profile_form':profile_form,
                                                            'registered':registered})
                                                            
                                                            
def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('paths:home'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('paths:dashboard'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            messages.error(request, 'Username or password is incorrect.')
            return redirect('paths:login')
    else:
        return render(request, 'paths/login.html')
        
@login_required(login_url='/paths/login/')
def user_logout(request):
    logout(request)
    return redirect(reverse('paths:home'))

@login_required(login_url='/paths/login/')
def previous_searches(request):
    
    prev_search_not_empty = True
    if(SearchResults.objects.filter(profile=request.user)):
        prev_search_not_empty = True
    else:
        prev_search_not_empty = False
        
    if not (request.user.is_authenticated):
        return redirect(reverse('paths:home'))
    if request.method == 'POST':
        prev_search_form = PrevSearches(user=request.user, data=request.POST)

        if prev_search_form.is_valid():
            prev_search_details = (prev_search_form.cleaned_data["prev_searches"] )

            prev_search_tags_list = []
            
            prev_searches_tags = prev_search_details.tags_searched.values("tag_name")
            for tag in list(prev_searches_tags):
                prev_search_tags_list.append(tag["tag_name"])
            print(prev_search_tags_list)
            request.session['search_tags'] = prev_search_tags_list

            return redirect('/paths/dashboard')
        else:
            messages.error(request, 'You have not selected a recent search.')
            return redirect('paths:previous-searches')
    else:
        prev_search_form = PrevSearches(user=request.user)

    
    return render(request, 'paths/previous-searches.html', context = {'prev_search_form':prev_search_form, 'prev_search_check':prev_search_not_empty })