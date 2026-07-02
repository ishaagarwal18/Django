"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from mypro import views
from rest_framework import routers

routers=routers.DefaultRouter()
routers.register(r"student",views.StudentViewSet)
routers.register(r"faculty",views.FacultyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("display",views.display,name="display"),
    path("update<int:id>",views.update,name="update"),
    path("delete<int:id>",views.delete,name="delete"),
    path("",include(routers.urls))
]
