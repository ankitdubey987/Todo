from django.urls import path
from todos import views

app_name='todos'
urlpatterns = [
    path('',views.TodoListView.as_view(),name='home'),
    path('create/',views.CreateTodoView.as_view(),name='create-todo'),
    path('done/<int:pk>/',views.markDone,name='done'),
]
