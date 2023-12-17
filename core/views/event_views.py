from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core import forms
from core.models import Event, Ticket, Company
from core.forms import EventForm
from django.utils.safestring import mark_safe

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
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Evento criado com sucesso!')
        return response

@method_decorator(login_required(login_url='login'), name='dispatch')
class EventDeleteView(DeleteView):
    model           = Event
    template_name   = 'core/event_delete.html'
    success_url = reverse_lazy('manage')

@login_required(login_url='login')
def event_delete(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()

    messages.success(request, mark_safe(f'Evento <strong>{event.title}</strong> deletado com sucesso!'))
    return redirect('/manage')

@login_required(login_url='login')
def event_tickets(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    tickets = Ticket.objects.filter(event__id = event_id, available = True)
    return render(request, 'core/event-tickets.html', {'tickets': tickets, 'event': event})

def event_update(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, mark_safe(f'Evento <strong>{event.title}</strong> atualizado com sucesso!'))
            return redirect('/manage')
    else:
        form = EventForm(instance=event)

    return render(request, 'core/manage/manage_event_update.html', {"form": form})
