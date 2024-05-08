from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Storm Talk",
      default_version='v1',
      description="API docs for Storm Talk server",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/post/', include('post.urls')),
    path('api/subscribe/', include('subscribe.urls')),
    path('api/news/', include('news.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
