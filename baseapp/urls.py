from django.urls import path
from .views import Login, Logout, TaskDelete, TaskList, TaskDetails, TaskCreate, TaskUpdate, RegisterPage

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    # path('logout', Logout.as_view(next_page = 'login'), name='logout'), // another method of do that logout
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetails.as_view(), name='task-details'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='edit-task'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete-task'),

]
