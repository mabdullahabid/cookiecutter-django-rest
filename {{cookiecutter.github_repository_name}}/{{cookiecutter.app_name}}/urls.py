from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include, reverse_lazy
from django.views.generic.base import RedirectView

from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .users.views import UserViewSet, UserCreateViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"users", UserCreateViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "{{ cookiecutter.app_title }}"
admin.site.site_title = "{{ cookiecutter.app_title }} Admin Portal"
admin.site.index_title = "{{ cookiecutter.app_title }} Admin"

# Swagger
api_info = openapi.Info(
    title="{{ cookiecutter.app_title }} API",
    default_version="v1",
    description="API Documentation for {{ cookiecutter.app_title }}",
    contact=openapi.Contact(email="{{ cookiecutter.email }}"),
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
]