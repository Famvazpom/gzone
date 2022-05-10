"""gzone URL Configuration

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

from django.urls import path,include
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('home/',HomeView.as_view(),name='home' ),
    path('perfil/',PerfilUpdateView.as_view(),name='profile-update'),
    path('',LandingView.as_view(),name='landing'),
    path('blog/',PostListView.as_view(),name='post-list'),
    path('blog/detail/<slug>/',PostDetailView.as_view(),name='post-detail'),
    path('blog/update/<slug>/',PostUpdateView.as_view(),name='post-update'),
    path('blog/create/',PostCreateView.as_view(),name='post-create'),
]
