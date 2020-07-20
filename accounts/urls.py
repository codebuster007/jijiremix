from django.urls import path, include
from djoser import views as djoser_views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from .views import UserLogoutAllView, UserProfileView

djoser_router = DefaultRouter()
djoser_router.register('accounts', djoser_views.UserViewSet)

urlpatterns = [

    path('accounts/login/', jwt_views.TokenObtainPairView.as_view(), name='accounts-login'),
    path('accounts/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='accounts-login-refresh'),
    path('accounts/logout/all/', UserLogoutAllView.as_view(), name='accounts-logout-all'),

    path('accounts/me/', UserProfileView.as_view(), name='accounts-me'),

    # accounts/ - account create
    path('', include(djoser_router.urls)),
]