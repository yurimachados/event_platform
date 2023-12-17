import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404, render
from core.models import Ticket, TicketPurchase
from core.forms import TicketForm
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='login')
def buy_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if not ticket.available:
        messages.error(request, 'O ingresso não está disponível.')
        return redirect('event-detail', pk=ticket.event.id)
    
    if ticket.quantity == 0:
        messages.error(request, 'O ingresso está esgotado.')
        return redirect('event-detail', pk=ticket.event.id)
        
    TicketPurchase.objects.create(ticket=ticket, buyer=request.user)
    messages.success(request, 'Ingresso comprado com sucesso!')
    ticket.update_quantity()
    return redirect('event-detail', pk=ticket.event.id)

@login_required(login_url='login')
def user_tickets(request):
    tickets = TicketPurchase.objects.filter(buyer=request.user)
    return render(request, 'core/user-tickets.html', {'tickets' : tickets})


@login_required(login_url='login')
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ingresso criado com sucesso!')
            return redirect('/manage')
    else:   
        form = TicketForm()
    return render(request, 'core/manage/ticket_create.html', {"form": form})

@login_required(login_url='login')
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket_name = ticket.name
    deletion_time = datetime.datetime.now().isoformat()
    ticket.delete()

    # Adicione os dados necessários à sessão
    request.session['ticket_deleted'] = True
    request.session['d_ticket'] = ticket_name
    request.session['d_time'] = deletion_time

    return redirect('/manage')

@login_required(login_url='login')
def ticket_update(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            ticket_name = ticket.name
            ticket_updated = True
            update_time = datetime.datetime.now().isoformat()

            request.session['ticket_updated'] = ticket_updated
            request.session['u_ticket'] = ticket_name
            request.session['u_time'] = update_time
            return redirect('/manage')
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'core/manage/ticket_update.html', {"form": form})

@csrf_exempt
def ticket_status_change(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if ticket.available == False:
        ticket.available = True
    else:
        ticket.available = False
    ticket.save()
    
    request.session['ticket_updated'] = True
    request.session['u_ticket'] = ticket.name
    request.session['u_time'] = datetime.datetime.now().isoformat()

    return JsonResponse(
        {
            'status': 'success',
        }
    )