from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event, Comment, Rating, Company
from django import forms

class EventListView(ListView):
    model = Event
    template_name = 'core/event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'core/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context
    
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['company','title', 'description', 'image', 'cover', 'location', 'date']
        widgets = {
            'date': forms.DateTimeInput(format=('%d-%m-%Y %H:%M'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'datetime-local'}),
        }

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'core/event_create.html'
    success_url = reverse_lazy('event-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        return context

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

class EventDeleteView(DeleteView):
    model           = Event
    template_name   = 'core/event_delete.html'
    success_url = reverse_lazy('event-list')
