from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
    

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'users', UserViewSet, basename='user')



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
    
]

urlpatterns += router.urls