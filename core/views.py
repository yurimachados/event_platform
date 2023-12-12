from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Company, Ticket, TicketPurchase
from .forms import RegistrationForm, EventForm
from django import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='login'), name='dispatch')
class EventListView(ListView):
    model = Event
    template_name = 'core/event_list.html'
    context_object_name = 'events'

@method_decorator(login_required(login_url='login'), name='dispatch')
class EventDetailView(DetailView):
    model = Event
    template_name = 'core/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context             = super().get_context_data(**kwargs)
        event               = self.get_object()
        tickets             = Ticket.objects.filter(event=event)
        context['comments'] = event.comments.all()
        context['tickets']  = tickets
        return context

@method_decorator(login_required(login_url='login'), name='dispatch')
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'core/event_create.html'
    success_url = reverse_lazy('event-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        return context

@method_decorator(login_required(login_url='login'), name='dispatch')
class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'core/event_update.html'
    success_url = reverse_lazy('event-list')

    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)

        if self.object:
            form.fields['date'].widget = forms.TextInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
        
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        return context

@method_decorator(login_required(login_url='login'), name='dispatch')
class EventDeleteView(DeleteView):
    model           = Event
    template_name   = 'core/event_delete.html'
    success_url = reverse_lazy('event-list')


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/event-list')
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {"form": form}) 

def event_tickets(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    tickets = Ticket.objects.filter(event__id = event_id, available = True)
    return render(request, 'core/event-tickets.html', {'tickets': tickets, 'event': event})