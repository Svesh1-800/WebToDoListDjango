from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteTask, CustomLoginView, LogoutView, RegisterPage

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name="login"),
    path('register/',RegisterPage.as_view(),name="register"),
    path('logout/',LogoutView.as_view(next_page="login"),name="logout"),
    path('', TaskList.as_view(),name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(),name='task'), 
    path('task-update/<int:pk>', TaskUpdate.as_view(),name='task-update'), 
    path('create', TaskCreate.as_view(),name='task-create'),
    path('task-delete/<int:pk>', DeleteTask.as_view(),name='task-delete'),
]
