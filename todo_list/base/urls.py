from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteTask


urlpatterns = [
    path('', TaskList.as_view(),name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(),name='task'), 
    path('task-update/<int:pk>', TaskUpdate.as_view(),name='task-update'), 
    path('create', TaskCreate.as_view(),name='task-create'),
    path('task-delete/<int:pk>', DeleteTask.as_view(),name='task-delete'),
]
