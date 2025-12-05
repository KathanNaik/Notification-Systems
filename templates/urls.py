from django.contrib import admin
from django.urls import path
from .views import TemplateCRUDView

urlpatterns = [
    path('', TemplateCRUDView.as_view(), name='template-list'),
    path('create/', TemplateCRUDView.as_view(), name='template-create'),
    path('<pk>/', TemplateCRUDView.as_view(), name='template-detail'),
    path('<pk>/update/', TemplateCRUDView.as_view(), name='template-update'),
    path('<pk>/delete/', TemplateCRUDView.as_view(), name='template-delete'),
]
