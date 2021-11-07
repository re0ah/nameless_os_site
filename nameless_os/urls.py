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
from bug_tracker.views import get_bug_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home_view.as_view()),
	path('save_page/', Manage.save_page),
	path('sign_in/', Sign_in_view.as_view()),
	path('sign_up/', Sign_up_view.as_view()),
	path('check_authorization/', check_authorization),
	path('logout/', redirect_logout),
	path('get_bug_report/', get_bug_report),
	re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]
