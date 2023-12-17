from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #event urls
    path('event-list/', EventListView.as_view(), name='event-list'),
    path('event-detail/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event-create/', EventCreateView.as_view(), name='event-create'),
    path('event-update/<int:event_id>/', views.event_update, name='event-update'),
    path('event-delete/<int:event_id>', views.event_delete, name='event-delete'),

    #ticket urls
    path('event-tickets/<int:event_id>', views.event_tickets, name='event-tickets'),
    path('buy-ticket/<int:ticket_id>', views.buy_ticket, name='buy-ticket'),
    path('user-tickets/', views.user_tickets, name='user-tickets'),
    # path('ticket-detail/<int:pk>/', views.ticket_details, name='ticket-details'),
    # path('ticket-detail/<int:pk>/', views.ticket_details, name='ticket-details'),

    #Management URLs
    path('manage/', views.manage, name='manage'),
    path('manage/event-update/<int:event_id>', views.event_update, name='event-update'),
    path('manage/ticket-create/', views.ticket_create, name='ticket-create'),
    path('manage/ticket-delete/<int:ticket_id>', views.ticket_delete, name='ticket-delete'),
    path('manage/ticket-update/<int:ticket_id>', views.ticket_update, name='ticket-update'),
    path('manage/ticket-status-change/<int:ticket_id>', views.ticket_status_change, name='ticket-status-change'),

    #login urls
    path('sign-up/', views.sign_up, name='sign_up'),
]