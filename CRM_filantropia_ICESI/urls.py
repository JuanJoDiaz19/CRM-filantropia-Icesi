"""
URL configuration for CRM_filantropia_ICESI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CRM_app.views.home import Home
from CRM_app.views.create_new import CreateNew
from CRM_app.views.delete_new import DeleteNew
from CRM_app.views.login import LogIn
from CRM_app.views.news import News
from CRM_app.views.singin import Singin
from CRM_app.views.sing_out import Singout
from CRM_app.views.singup import Singup
from CRM_app.views.tasks import Tasks
from CRM_app.views.allies import Allies
from CRM_app.views.calendar import Calendar
from CRM_app.views.reports import Reports
from CRM_app.views.investigations_projects import InvestigationsProjects
from CRM_app.views.config import Config
from CRM_app.views.ally import Ally
from CRM_app.views.add_contact import AddContact
from CRM_app.views.add_allie import Add_allie
from CRM_app.views.add_intern import Add_intern
from CRM_app.views.interns import Interns
from CRM_app.views.donation import donation_
from CRM_app.views.create_meeting import create_meeting
from CRM_app.views.create_event import create_event
from CRM_app.views.add_donation import AddDonation
from CRM_app.views.calendar import Calendar
from CRM_app.views.single_page_investigation_project import InvestigationProject
from CRM_app.views.single_ally_investigation import InvestigationsProjectsAlly
from CRM_app.views.add_investigation_project import AddInvestigationProject
from CRM_app.views.edit_ally import EditAlly
from CRM_app.views.edit_contact import EditContact
from CRM_app.views.edit_intern import EditIntern
from CRM_app.views.edit_investigation_project import EditInvestigationProject
from CRM_app.views.add_publication import AddPublication
from CRM_app.views.register_user import RegisterUser
from CRM_app.views.cedep_marketing_home import Cedep_marketing_home




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LogIn.as_view(), name="login"),
    path('signup/', Singup.as_view(), name="signup"),
    path('signin/', Singin.as_view(), name="signin"),
    path('tasks/', Tasks.as_view(), name="tasks"),
    path('home/', News.as_view(), name="home"),
    path('calendar/<str:allie_id>', Calendar.as_view(), name="calendar"),
    path('reports/', Reports.as_view(), name="reports"),
    path('investigations/', InvestigationsProjects.as_view(), name="investigations"),
    path('config/', Config.as_view(), name="config"),
    path('allies/add_ally/', Add_allie.as_view(), name="add_allie"),
    path('interns/add_intern/<int:allie__id>/', Add_intern.as_view(), name="add_intern"),
    path('logout/', Singout.as_view(), name="logout"),
    path('news/', News.as_view(), name="news"),
    path('create_new/', CreateNew.as_view(), name='create_new'),
    path('delete_new/<int:new_id>/', DeleteNew.as_view(), name='delete_new'),
    path('allies/', Allies.as_view(), name='allies'),
    path('interns/<int:allie__id>', Interns.as_view(), name='interns'),
    path('allies/<int:allie_id>/', Ally.as_view(), name="ally"),
    path('add_contact/<int:allie_id>/', AddContact.as_view(), name='add_contact'),
    path('donations/<int:allie__id>', donation_.as_view(), name="donation"),
    path('calendar/create_meeting/', create_meeting.as_view(), name="create_meeting"),
    path('calendar/create_event/', create_event.as_view(), name="create_event"),
    path('allies/<int:allie__id>/add-donation/', AddDonation.as_view(), name="add_donation"),
    path('investigation/<int:project__id>/', InvestigationProject.as_view(), name="single_page_investigation_projects"),
    path("allies/investigation/<int:allie__id>", InvestigationsProjectsAlly.as_view(), name="single-page-ally-investigation"),
    path("add_investigation_project/", AddInvestigationProject.as_view(), name="add_investigation_project"),
    path('edit_ally/<int:allie_id>/', EditAlly.as_view(), name='edit_ally'),
    path('edit_contact/<int:allie_id>/<int:contact_info_id>/', EditContact.as_view(), name='edit_contact'),
    path('edit_intern/<int:allie_id>/<int:intern_id>/', EditIntern.as_view(), name='edit_intern'),
    path('edit_investigation_project/<int:project__id>/', EditInvestigationProject.as_view(), name='edit_investigation_project'),
    path("add_publication/<int:project__id>/", AddPublication.as_view(), name="add_publication"),
    path("register/", RegisterUser.as_view(), name='register'),
    path("cedep/", Cedep_marketing_home.as_view(), name="CEDEP_view"),
]
    