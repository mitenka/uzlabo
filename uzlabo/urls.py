from django.contrib import admin
from django.urls import path, include
from ideas import views as ideas_views

urlpatterns = [
    path('ideas/', ideas_views.index, name='ideas-index'),

    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
