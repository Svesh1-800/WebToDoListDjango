from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, DeleteTask, CustomLoginView, LogoutView, RegisterPage

app_name = 'todo'

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name="login"),
    path('register/',RegisterPage.as_view(),name="register"),
    path('logout/',LogoutView.as_view(next_page="todo:login"),name="logout"),
    path('', TaskList.as_view(),name='tasks'), 
    path('task-update/<int:pk>', TaskUpdate.as_view(),name='task-update'), 
    path('create', TaskCreate.as_view(),name='task-create'),
    path('task-delete/<int:pk>', DeleteTask.as_view(),name='task-delete'),
]
