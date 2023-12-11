from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
from . import views

urlpatterns = [
    path('event-list/', EventListView.as_view(), name='event-list'),
    path('event-detail/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event-create/', EventCreateView.as_view(), name='event-create'),
    path('event-update/<int:pk>/', EventUpdateView.as_view(), name='event-update'),
    path('event-delete/<int:pk>', EventDeleteView.as_view(), name='event-delete'),

    path('sign-up/', views.sign_up, name='sign_up'),
]