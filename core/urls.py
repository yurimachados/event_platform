from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
from . import views

urlpatterns = [
    #event urls
    path('event-list/', EventListView.as_view(), name='event-list'),
    path('event-detail/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event-create/', EventCreateView.as_view(), name='event-create'),
    path('event-update/<int:pk>/', EventUpdateView.as_view(), name='event-update'),
    path('event-delete/<int:pk>', EventDeleteView.as_view(), name='event-delete'),

    #ticket urls
    path('event-tickets/<int:event_id>', views.event_tickets, name='event-tickets'),
    path('buy-ticket/<int:ticket_id>', views.buy_ticket, name='buy-ticket'),
    # path('ticket-detail/<int:pk>/', views.ticket_details, name='ticket-details'),
    # path('ticket-detail/<int:pk>/', views.ticket_details, name='ticket-details'),

    #login urls
    path('sign-up/', views.sign_up, name='sign_up'),
]