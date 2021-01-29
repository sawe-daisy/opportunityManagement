from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import register, PostCreateView, PostListView, PostDetailView, OpportunityCreateView

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', register, name='home'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('opportunity/', OpportunityCreateView.as_view(), name='oppCreate'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/list/', PostListView.as_view(), name='account'),
    path('api/logout/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]