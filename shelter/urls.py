from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),
    
    # Pet pages
    path('pets/', views.PetListView.as_view(), name='pets'),
    path('pet/<int:pk>/<slug:slug>/', views.PetDetailView.as_view(), name='pet_detail'),
    
    # Information pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success-stories/', views.success_stories, name='success_stories'),
    
    # Adoption
    path('adoption/', views.adoption_process, name='adoption_process'),
    path('adoption/apply/', views.adoption_application, name='adoption_application'),
    path('adoption/apply/<int:pet_id>/', views.adoption_application, name='adoption_application_pet'),
]
