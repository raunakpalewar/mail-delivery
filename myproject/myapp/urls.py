from django.urls import path,re_path
from django.conf.urls.static import static
from django.conf import settings
from .import views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .import views



schema_view = get_schema_view(
   openapi.Info(
      title="Mail Delivery",
      default_version='r1',
      description="For Resume Builder",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
        path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
