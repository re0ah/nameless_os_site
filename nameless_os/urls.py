"""nameless_os URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
# Для Media файлов
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from home.views import Home_view, Manage
from sign.views import Sign_in_view, Sign_up_view, redirect_logout, check_authorization
from bug_tracker.views import Manage_bug_tracker
from task.views import Manage_task_tracker

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home_view.as_view()),
	path('save_page/', Manage.save_page),
	path('sign_in/', Sign_in_view.as_view()),
	path('sign_up/', Sign_up_view.as_view()),
	path('check_authorization/', check_authorization),
	path('logout/', redirect_logout),
	path('get_bug_report/', Manage_bug_tracker.get_bug_report),
	path('get_bug_list_current/', Manage_bug_tracker.get_bug_list_current),
	path('get_bug_list_solved/', Manage_bug_tracker.get_bug_list_solved),
	path('get_task_offer/', Manage_task_tracker.get_task_offer),
	path('get_task_list_current/', Manage_task_tracker.get_task_list_current),
	path('get_task_list_solved/', Manage_task_tracker.get_task_list_solved),
	path('get_task_list_deffered/', Manage_task_tracker.get_task_list_deffered),
	re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]
