from django.urls import path
from .views import UserLoginView,RegisterUserView,LogoutView,ProfileView,ProfileEditView
app_name='users'
urlpatterns = [
    path('profile/',ProfileView.as_view(),name='profile'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('register/',RegisterUserView.as_view(),name='signup'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('edit/<int:pk>/',ProfileEditView.as_view(),name='edit'),
]