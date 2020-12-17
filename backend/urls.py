"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

#from backend.core import views

#from backend.partners import views

from backend.authentication import views

urlpatterns = [

    #path('signup/', views.signup, name='signup'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('upload/', views.upload, name = 'upload-partners'),
    # path('update/<int:partners_id>', views.update_partners),
    # path('delete/<int:partners_id>', views.delete_partners)


    #path('admin/', admin.site.urls),
    path('authentication/Signup/', views.SignupView.as_view(), name='Signup'),
    path('', views.Dashboard, name='dashboard'),
    path('authentication/logout/', views.Logout, name='logout'),
    path('authentication/login/', views.LoginView.as_view(), name='login'),
]
