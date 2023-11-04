"""ecomproj URL Configuration

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
from django.urls import path, include
from user_login.views import *
from admin_user.views import *
from home.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    # path('',reg,name='reg'),
    # path('login',login,name='login'),
    # path('index',index,name='index'),
    # path('logout',logout,name='logout'),
    # path('admin_index',admin_index,name='admin_index'),
    # path('edit_user<uid>',edit_user,name='edit_user'),
    # path('search',search,name='search'),
    # path('delete_user<uid>',delete_user,name='delete_user'),
    # path('admin_login',admin_login,name='admin_login'),
    # path('admin_logout',admin_logout,name='admin_logout'),
    
]
