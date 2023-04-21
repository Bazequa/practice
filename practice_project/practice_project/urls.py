"""practice_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from practice_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.orm),
    path('student',views.student),
    path('teacher',views.teacher),
    path('orm1',views.orm1),
    path('orm2',views.orm2),
    path('orm3',views.orm3),
]
