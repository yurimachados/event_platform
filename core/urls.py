from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #event urls
    path('event-list/', EventListView.as_view(), name='event-list'),
    path('event-detail/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event-create/', EventCreateView.as_view(), name='event-create'),
    path('event-update/<int:pk>/', EventUpdateView.as_view(), name='event-update'),
    path('event-delete/<int:pk>', EventDeleteView.as_view(), name='event-delete'),

    #ticket urls
    path('event-tickets/<int:event_id>', views.event_tickets, name='event-tickets'),
    path('buy-ticket/<int:ticket_id>', views.buy_ticket, name='buy-ticket'),
    path('user-tickets/', views.user_tickets, name='user-tickets'),
    # path('ticket-detail/<int:pk>/', views.ticket_details, name='ticket-details'),
    # path('ticket-detail/<int:pk>/', views.ticket_details, name='ticket-details'),

    #Management URLs
    path('manage/', views.manage, name='manage'),
    path('manage/event-update/<int:event_id>', views.manage_event_update, name='manage-event-update'),
    path('manage/ticket-create/', views.ticket_create, name='ticket-create'),
    path('manage/ticket-delete/<int:ticket_id>', views.ticket_delete, name='ticket-delete'),

    #login urls
    path('sign-up/', views.sign_up, name='sign_up'),
]