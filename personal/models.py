from django.db import models

# โมเดลสำหรับข้อมูลส่วนตัว
class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name

# โมเดลสำหรับประสบการณ์ทำงาน
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"

# โมเดลสำหรับโครงการ (Projects)
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

# โมเดลสำหรับใบรับรอง (Certifications)
class Certification(models.Model):
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    credential_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# โมเดลสำหรับแกลเลอรีรูปภาพ
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title

# โมเดลสำหรับการศึกษา
class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"
