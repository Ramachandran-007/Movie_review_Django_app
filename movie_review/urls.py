"""
URL configuration for movie_review project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from movie import views
from users import views as users_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addmovie/',views.add_movie_view,name='addmoive'),
    path('',views.home_view,name='home'),
    path('review/<int:id>/',views.review_view,name='review'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('register/',users_view.Register_view,name='register'),
    path('login/',users_view.login_view,name='login'),
    path('logout/',users_view.logout_view,name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)