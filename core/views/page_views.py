import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from core.forms import RegistrationForm
from core.models import Event, Ticket, TicketPurchase

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
def home(request):
    return render(request, 'core/home.html')

@login_required(login_url='login')
def manage(request):

    # Verifica se o ticket foi deletado
    if 'ticket_deleted' in request.session:
        ticket_deleted = request.session.get('ticket_deleted')
        d_ticket = request.session['d_ticket']
        d_time_str = request.session['d_time']
        d_time = datetime.datetime.fromisoformat(d_time_str) - datetime.timedelta(hours=3)

        del request.session['ticket_deleted']
        del request.session['d_ticket']
        del request.session['d_time']
    else:
        ticket_deleted = False
        d_ticket = None
        d_time = None

    # Verifica se o ticket foi atualizado
    if 'ticket_updated' in request.session:
        ticket_updated = request.session.get('ticket_updated')
        u_ticket = request.session['u_ticket']
        u_time_str = request.session['u_time']
        u_time = datetime.datetime.fromisoformat(u_time_str) - datetime.timedelta(hours=3)

        del request.session['ticket_updated']
        del request.session['u_ticket']
        del request.session['u_time']
    else:
        ticket_updated = False
        u_ticket = None
        u_time = None

    events = Event.objects.all()
    tickets = Ticket.objects.all()
    tickets_purchases = TicketPurchase.objects.all()

    return render(request, 'core/manage/manage.html', {
        'events': events,
        'tickets': tickets,
        'tickets_purchases': tickets_purchases,
        'ticket_deleted': ticket_deleted,
        'd_ticket': d_ticket,
        'd_time': d_time,
        'ticket_updated': ticket_updated,
        'u_ticket': u_ticket,
        'u_time': u_time
    })