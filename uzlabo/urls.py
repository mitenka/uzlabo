from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from ideas import views as ideas_views

urlpatterns = i18n_patterns(
    path('ideas/', ideas_views.index, name='ideas-index'),
    path('ideas/<int:pk>/', ideas_views.details, name='ideas-details'),
    path('ideas/new/', ideas_views.new, name='ideas-new'),

    path('pages/', include('django.contrib.flatpages.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
