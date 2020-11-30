from django.contrib import admin
from django.urls import path
from ideas import views as ideas_views

urlpatterns = [
    path('ideas/', ideas_views.index, name='ideas-index'),
    path('admin/', admin.site.urls),
]
