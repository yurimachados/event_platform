import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404, render
from core.models import Ticket, TicketPurchase
from core.forms import TicketForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe


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
    messages.success(request, mark_safe(f'Ingresso <strong>{ticket.name}</strong> comprado com sucesso!'))
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
    ticket.delete()

    messages.success(request, mark_safe(f'Ingresso <strong>{ticket.name}</strong> deletado com sucesso!'))
    return redirect('/manage')

@login_required(login_url='login')
def ticket_update(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, mark_safe(f'Ingresso <strong>{ticket.name}</strong> atualizado com sucesso!'))
            return redirect('/manage')
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'core/manage/ticket_update.html', {"form": form})

@csrf_exempt
@login_required(login_url='login')
def ticket_status_change(ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if ticket.available == False:
        ticket.available = True
        message = f'Ingresso <strong>{ticket.name}</strong> agora está disponível!'
    else:
        ticket.available = False
        message = f'Ingresso <strong>{ticket.name}</strong> agora está indisponível!'
    
    ticket.save()

    return JsonResponse(
        {
            'status': 'success',
            'message': message
        }
    )