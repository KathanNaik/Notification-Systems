from django.contrib import admin
from django.urls import path
from .views import EventCRUDView

urlpatterns = [
    path('', EventCRUDView.as_view(), name='event-list'),
    path('create/', EventCRUDView.as_view(), name='event-create'),
    path('<pk>/', EventCRUDView.as_view(), name='event-detail'),
    path('<pk>/update/', EventCRUDView.as_view(), name='event-update'),
    path('<pk>/delete/', EventCRUDView.as_view(), name='event-delete'),
]
