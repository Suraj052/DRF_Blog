from django.urls import path
from .views import CustomUserCreate,UserList
app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('userlist/', UserList.as_view(), name="user_list"),

    # path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
    #      name='blacklist')
]