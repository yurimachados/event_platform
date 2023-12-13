from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Company, Ticket, TicketPurchase
from .forms import RegistrationForm, EventForm, TicketForm
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
    success_url = reverse_lazy('manage')

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
    success_url = reverse_lazy('manage')


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

@login_required(login_url='login')
def event_tickets(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    tickets = Ticket.objects.filter(event__id = event_id, available = True)
    return render(request, 'core/event-tickets.html', {'tickets': tickets, 'event': event})

@login_required(login_url='login')
def buy_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    TicketPurchase.objects.create(ticket=ticket, buyer=request.user)
    return redirect('/event-list')

@login_required(login_url='login')
def user_tickets(request):
    tickets = TicketPurchase.objects.filter(buyer=request.user)
    return render(request, 'core/user-tickets.html', {'tickets' : tickets})

@login_required(login_url='login')
def home(request):
    return render(request, 'core/home.html')

@login_required(login_url='login')
def manage(request):
    events = Event.objects.all()
    tickets = Ticket.objects.all()
    tickets_purchases = TicketPurchase.objects.all()
    return render(request, 'core/manage/manage.html', {'events': events, 'tickets': tickets, 'tickets_purchases': tickets_purchases})

def manage_event_update(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/manage')
    else:
        form = EventForm(instance=event)

    return render(request, 'core/manage/manage_event_update.html', {"form": form})

@login_required(login_url='login')
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/manage')
    else:   
        form = TicketForm()
    return render(request, 'core/manage/ticket_create.html', {"form": form})