from django.urls import path
from paths import views

app_name = 'paths'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('resource-upload/', views.upload_resource, name='resource-upload'),
    path('previous-searches/', views.previous_searches, name='previous-searches'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
]
