from django.urls import path
from .views import *

urlpatterns = [
    # Users URLs
    path('users', UsersListCreateView.as_view(), name='users-list-create'),
    path('users/<int:pk>/', UsersRetrieveUpdateDeleteView.as_view(), name='users-detail'),

    # Tasks URLs
    path('tasks', TasksListCreateView.as_view(), name='tasks-list-create'),
    path('tasks/<int:pk>/', TasksRetrieveUpdateDeleteView.as_view(), name='tasks-detail'),

    # CCode URLs
    path('ccode/', CCodeListCreateView.as_view(), name='ccode-list-create'),
    path('ccode/<int:pk>/', CCodeRetrieveUpdateDeleteView.as_view(), name='ccode-detail'),

    # AccessControl URLs
    path('accesscontrol', AccessControlListCreateView.as_view(), name='accesscontrol-list-create'),
    path('accesscontrol/<int:pk>/', AccessControlRetrieveUpdateDeleteView.as_view(), name='accesscontrol-detail'),
]
