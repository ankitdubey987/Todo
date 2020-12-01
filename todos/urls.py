from django.urls import path
from todos import views

app_name='todos'
urlpatterns = [
    path('',views.TodoListView.as_view(),name='home'),
    path('create/',views.CreateTodoView.as_view(),name='create-todo'),
    path('done/<int:pk>/',views.markDone,name='done'),
    path('edit/<int:pk>/',views.TodoUpdateView.as_view(),name='edit'),
    path('delete/<int:pk>/',views.TodoRemoveView.as_view(),name='remove'),
]
