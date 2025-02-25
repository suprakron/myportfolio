from django.shortcuts import render,redirect
from .models import Profile, Experience, Project, Certification, Gallery, Education
from .forms import ProfileForm

def home(request):
    """
    หน้า Home: แสดงข้อมูลส่วนตัว (Profile)
    """
    profile = Profile.objects.first()  # ดึงข้อมูลโปรไฟล์ตัวแรก (หรือปรับตามต้องการ)
    context = {
        'profile': profile,
    }
    return render(request, 'home.html', context)

def experience(request):
    """
    หน้า Experience: แสดงประสบการณ์การทำงานทั้งหมด
    """
    experiences = Experience.objects.all()
    context = {
        'experiences': experiences,
    }
    return render(request, 'experience.html', context)

def projects(request):
    """
    หน้า Projects: แสดงโครงการที่เคยทำ
    """
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'projects.html', context)

def certifications(request):
    """
    หน้า Certifications: แสดงใบรับรองและการฝึกอบรม
    """
    certifications = Certification.objects.all()
    context = {
        'certifications': certifications,
    }
    return render(request, 'certifications.html', context)

def gallery(request):
    """
    หน้า Gallery: แสดงแกลเลอรีรูปภาพ
    """
    images = Gallery.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'gallery.html', context)

def education(request):
    """
    หน้า Education: แสดงประวัติการศึกษา
    """
    education = Education.objects.all()
    context = {
        'education': education,
    }
    return render(request, 'education.html', context)

def contact(request):
    """
    หน้า Contact: แสดงข้อมูลการติดต่อ
    """
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }
    return render(request, 'contact.html', context)


def edit_profile(request):
    profile = Profile.objects.first()  # หรือใช้ get_object_or_404()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})