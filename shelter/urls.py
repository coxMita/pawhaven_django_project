from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('adoption/process/', views.adoption_process, name='adoption_process'),
    path('adoption/apply/', views.adoption_application, name='adoption_application'),
    path('adoption/apply/<int:pet_id>/', views.adoption_application, name='adoption_application_pet'),

    # If you kept a custom site login, keep its name distinct:
    path('login/', auth_views.LoginView.as_view(
        template_name='shelter/login.html',
        redirect_authenticated_user=True
    ), name='site_login'),


    # Gate (what your "Apply" buttons should link to)
    path('adoption/start/', views.adoption_gate, name='adoption_gate'),
    path('adoption/start/<int:pet_id>/', views.adoption_gate, name='adoption_gate_pet'),

    # Account area
    path('register/', views.register, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('account/', views.account, name='account'),
    path('account/applications/', views.user_applications, name='user_applications'),
    path('account/edit/', views.edit_profile, name='edit_profile'),
]
