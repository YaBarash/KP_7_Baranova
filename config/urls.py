from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        # название нашей документации
        title="Habits API",
        # версия документации
        default_version='v1',
        # описание нашей документации
        description="Habits API description",
        terms_of_service="https://localhost/policies/terms/",
        contact=openapi.Contact(email="titarenko.analytics@yendex.ru"),
        license=openapi.License(name="Habits License"),
    ),
    public=True,
    # в разрешениях можем сделать доступ только авторизованным пользователям.
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('habits/', include('habits.urls', namespace='habits')),
    path('users/', include('users.urls', namespace='users')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]