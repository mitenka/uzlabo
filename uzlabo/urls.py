from django.contrib import admin
from django.urls import path, include
from ideas import views as ideas_views

urlpatterns = [
    path('ideas/', ideas_views.index, name='ideas-index'),
    path('ideas/<int:pk>', ideas_views.details, name='ideas-details'),
    path('ideas/new/', ideas_views.new, name='ideas-new'),

    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
