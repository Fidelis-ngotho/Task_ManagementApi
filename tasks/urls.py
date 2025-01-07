from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import RedirectView
from rest_framework.views import APIView
from .views import APIRootView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # API root
    path('api/', APIRootView.as_view(), name='api-root'),

    # JWT Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Browsable API login/logout
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_auth')),

    # Favicon
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]

# Include router-generated URLs
urlpatterns += router.urls
