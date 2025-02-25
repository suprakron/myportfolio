from django import forms
from .models import Profile, Experience, Project, Certification, Gallery, Education

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'profile_image', 'email', 'phone', 'website']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'github_link', 'demo_link']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'organization', 'issue_date', 'credential_url']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
        }

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
