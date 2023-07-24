from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import *
from .forms import *
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import client_required, personell_required, management_required
# Create your views here.
def dashboard(request):
	context={
			"data":1
			}
	
	return render(request,'index.html',context)

class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'client/sign_up.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('client_dashboard')
    

class PersonellSignUpView(CreateView):
    model = User
    form_class = PersonellSignUpForm
    template_name = 'personell/sign_up.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'personell'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('personell_dashboard')


class ManagementSignUpView(CreateView):
    model = User
    form_class = PersonellSignUpForm
    template_name = 'management/sign_up.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'management'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('management_dashboard')
    


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_client:
                return reverse('client_dashboard')
            elif user.is_personell:
                return reverse('personell_dashboard')
            elif user.is_management:
                return reverse('management_dashboard')
        else:
            return reverse('login')
        


@login_required
@client_required
def client_dashboard(request):
    projects =  Project.objects.filter(client=request.user.client)
    context = {
        'projects': projects
    }
    return render(request, 'client/dashboard.html', context)



@login_required
@personell_required
def personell_dashboard(request):
    projects = Project.objects.filter(project_manager=request.user.personell)
    reports = Report.objects.all()
    context = {
        'projects': projects,
        'reports': reports
    }
    return render(request, 'personell/dashboard.html', context)



@login_required
@management_required
def management_dashboard(request):
    projects = Project.objects.all()
    reports = Report.objects.all()
    context = {
        'projects': projects,
        'reports': reports
    }
    return render(request, 'management/dashboard.html', context)


@login_required
@personell_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.project_manager = request.user.personell
            project.save()
            return redirect('personell_dashboard')
    else:
        form = ProjectForm()
    return render(request, 'personell/create_project.html', {'form': form})


@login_required
@personell_required
def create_report(request, project_id):
    project = Project.objects.get(id=project_id)
    if Report.objects.filter(project=project, personell=request.user.personell).exists():
        return redirect('personell_dashboard')
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.personell = request.user.personell
            report.project = project
            report.save()
            return redirect('personell_dashboard')
    else:
        form = ReportForm()
    return render(request, 'personell/create_report.html', {'form': form, 'project': project})


@login_required
@client_required
def client_report_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    """ if Report.objects.filter(project=project, client=request.user.client).exists():
        report = Report.objects.get(project=project, client=request.user.client)
        approved = True
    else:
        report = None
        approved = False"""
    
    if Report.objects.filter(project=project).exists():
        report = Report.objects.get(project=project)
        approved = True
    else:
        report = None
        approved = False
    context = {
        'project': project,
        'report': report,
        'approved': approved
    }
    return render(request, 'client/report_detail.html', context)


@login_required 
@personell_required
def personell_project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    if project.project_manager != request.user.personell:
        return redirect('personell_dashboard')
    reports = Report.objects.filter(project=project)
    context = {
        'project': project,
        'reports': reports
    }
    return render(request, 'personell/project_detail.html', context)