from django.urls import path
from .views import (
    UserSessionListView,
    SessionDetailView,
    SessionCreateView,
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/<str:username>/', UserSessionListView.as_view(), name='user-sessions'),
    path('session/<int:pk>/', SessionDetailView.as_view(), name='session-detail'),
    path('session/new/', SessionCreateView.as_view(), name='session-create'),
]