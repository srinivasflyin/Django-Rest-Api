from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
urlpatterns = [
    path('createuser', views.createUser, name='createuser'),
    path('token', TokenObtainPairView.as_view(), name="tokenobtain"),
    path('refreshtoken', TokenRefreshView.as_view(), name="refreshtoken"),
    path('login', views.login, name= 'login')
]