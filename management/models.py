from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_client = models.BooleanField(default=False)
    is_personell = models.BooleanField(default=False)
    is_management = models.BooleanField(default=False)
 
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='client')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=False, blank=True, null=True)
    is_guest = models.BooleanField(default=False, blank=True, null=True)
    banned = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)    
    def __str__(self):
        return self.user.username   

class Personell(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='personell')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    national_id = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False, blank=True, null=True)
    banned = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)    
    def __str__(self):
        return self.user.username   

class Management(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='management')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    national_id = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    experience = models.TextField(max_length=100, blank=True, null=True)
    education = models.TextField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=False, blank=True, null=True)
    banned = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)    
    def __str__(self):
        return self.user.username   

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255)
    address_location = models.TextField(blank=True, null=True)
    project_manager = models.ForeignKey(Personell, on_delete=models.CASCADE, related_name='project_managers')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='project_clients')
    created_at = models.DateTimeField(default=timezone.now)    
    def __str__(self):
        return self.name  

class Report(models.Model):
    title= models.CharField(max_length=255,blank=True, null=True)
    date = models.DateField(default=timezone.now)
    report = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projects')
    personell = models.ForeignKey(Personell, on_delete=models.CASCADE, related_name='personell_reporting')
    image_update = models.BooleanField(default=False, blank=True, null=True)
    video_update = models.BooleanField(default=False, blank=True, null=True)
    cctv_link = models.BooleanField(default=False, blank=True, null=True)
    approved = models.BooleanField(default=False, blank=True, null=True)
    reviewed_by_admin = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)    
    def __str__(self):
        return self.title
 

class ProjectDocument(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_documents')
    document_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    upload = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)    
    def __str__(self):
        return self.document_name