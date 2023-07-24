from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [  
    path("", views.client_dashboard, name="client_dashboard"),
    path("personell/", views.personell_dashboard, name="personell_dashboard"),
    path("management/", views.management_dashboard, name="management_dashboard"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/client/", views.ClientSignUpView.as_view(), name="client_signup"),
    path("signup/personell/", views.PersonellSignUpView.as_view(), name="personell_signup"),
    path("signup/management/", views.ManagementSignUpView.as_view(), name="management_signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("management/project/create/", views.create_project, name="create_project"),
    path("project/<int:project_id>/report/", views.create_report, name="create_report"),
    path("project/<int:project_id>/", views.client_report_detail, name="client_report_detail"),
    path("personell/project/<int:project_id>/", views.personell_project_detail, name="personell_project_detail"),
 
]
