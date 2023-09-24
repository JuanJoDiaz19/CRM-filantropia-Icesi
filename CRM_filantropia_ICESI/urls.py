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
from CRM_app.views.news import News
from CRM_app.views.singin import Singin
from CRM_app.views.sing_out import Singout
from CRM_app.views.singup import Singup
from CRM_app.views.tasks import Tasks
from CRM_app.views.allie_view import allies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
    path('signup/', Singup.as_view(), name="signup"),
    path('signin/', Singin.as_view(), name="signin"),
    path('tasks/', Tasks.as_view(), name="tasks"),
    path('logout/', Singout.as_view(), name="logout"),
    path('news/', News.as_view(), name="news"),
    path('create_new/', CreateNew.as_view(), name='create_new'),
    path('delete_new/<int:new_id>/', DeleteNew.as_view(), name='delete_new'),
    path('allies/', allies.as_view(), name='allie_view'),

]
