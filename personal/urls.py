from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
    path('certifications/', views.certifications, name='certifications'),
    path('gallery/', views.gallery, name='gallery'),
    path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
]
