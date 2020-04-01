from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from .views import current_user, UserList


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.ContactListCreate.as_view()),
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('auth/', obtain_jwt_token)
]

