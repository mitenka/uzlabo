from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ideas import views as ideas_views

urlpatterns = [
    path('ideas/', ideas_views.index, name='ideas-index'),
    path('ideas/<int:pk>', ideas_views.details, name='ideas-details'),
    path('ideas/new/', ideas_views.new, name='ideas-new'),

    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
