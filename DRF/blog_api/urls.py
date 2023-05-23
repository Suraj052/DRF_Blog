from django.urls import path, include
from .views import PostList,CategoryList
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()
router.register('posts',PostList, basename='post') 
router.register('category',CategoryList, basename='category')
urlpatterns = router.urls

# urlpatterns = [
# path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
# path('', PostList.as_view(), name='listcreate'),
# ]

