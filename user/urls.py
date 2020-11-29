from django.urls import path
from .views import UserLoginView,RegisterUserView,LogoutView
app_name='users'
urlpatterns = [
    path('login/',UserLoginView.as_view(),name='login'),
    path('register/',RegisterUserView.as_view(),name='signup'),
    path('logout/',LogoutView.as_view(),name='logout'),
]