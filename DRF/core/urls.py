from re import I
from django.contrib import admin
from blog_api.views import CategoryList
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls',namespace='blog')),

    path('api/',include('blog_api.urls',namespace='blog_api')),
    
    path('api/user/',include('users.urls',namespace='users')),
    path('api-auth/',include('rest_framework.urls',namespace = 'rest_framework')),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('docs/',include_docs_urls(title="BlogAPI")),
    path('schema',get_schema_view(
        title="BlogAPI ",
        description="API for blog",
        version="1.0.0"
        ),name='openapi-schema'
    ),

 
]
 