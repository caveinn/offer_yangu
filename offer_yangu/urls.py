"""offer_yangu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from django.views.generic.base import RedirectView

admin.site.site_header = "OfferYangu Admin"
admin.site.site_title = "OfferYangu Admin Portal"
admin.site.index_title = "Welcome to OfferYangu Admin Portal"

schema_view = get_schema_view(
    openapi.Info(
        title="Offer Yangu API",
        default_version='v1',
        description="The official Offer Yangu API documentation",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

admin.site.site_url = 'https://development.offeryangu.co.ke/' 

urlpatterns = [
    path('',  RedirectView.as_view(url='docs')),
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('api/', include("offer_yangu.authentication.urls", namespace="authentication")),
    path('api/', include("offer_yangu.offers.urls", namespace="offers"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
