from django.urls import path
from .views import ModelAListView

urlpatterns = [
    path('model_a/', ModelAListView.as_view(), name='model_a_list_create'),
    path('model_a/<int:pk>/', ModelAListView.as_view(), name='model_a_list_create'),
]
