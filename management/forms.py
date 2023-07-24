from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import *
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ClientSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput())
    password2 = forms.CharField(label=("Confirm Password"), widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        if commit:
            user.save()
        client = Client.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'))
        return user
    


class PersonellSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput())
    password2 = forms.CharField(label=("Confirm Password"), widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_personell = True
        if commit:
            user.save()
        personell = Personell.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'))
        return user
    



class ManagementSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput())
    password2 = forms.CharField(label=("Confirm Password"), widget=forms.PasswordInput())

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_management = True
        if commit:
            user.save()
        client = Management.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'))
        return user
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    


class ProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())
    

    class Meta:
        model = Project
        fields = ('name', 'description', 'status', 'project_manager', 'client')


class ProjectDocumentForm(forms.ModelForm):
    #project = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = ProjectDocument
        fields = ('project', 'document_name', 'description', 'upload')

class ReportForm(forms.ModelForm):
   # question = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Report
        fields = ('date','title', 'report', 'project' )