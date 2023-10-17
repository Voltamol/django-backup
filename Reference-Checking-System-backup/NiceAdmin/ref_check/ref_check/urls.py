"""
URL configuration for ref_check project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('analytics.urls')),
    path('candidate_profile_view', include('analytics.urls')),
    path('update', include('analytics.urls')),
    path('Candidate_Reports', include('analytics.urls')),
    path('candidates', include('analytics.urls')),
    path('candidate_idx', include('analytics.urls')),
    path('candidate_signup', include('analytics.urls')),
    path('login', include('analytics.urls')),
    path('questionnaire', include('analytics.urls')),
    path('referee_candidates_list', include('analytics.urls')),
    path('thank_you', include('analytics.urls')),
    path('email',include('mail.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
