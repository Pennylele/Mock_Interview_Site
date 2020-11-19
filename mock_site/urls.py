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
    path('session/<uuid:pk>/', SessionDetailView.as_view(), name='session-detail'),
    path('session/new/', SessionCreateView.as_view(), name='session-create'),
    path('<str:room_name>/', views.session_detail, name="session_detail"),
    path('ajax/result/', views.result, name="result")
]