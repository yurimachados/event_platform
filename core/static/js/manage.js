$(document).ready(function(){
    $('.ticket-available-input').on('change', function(){
        let ticketId = $(this).data('id');
        let available = $(this).is(':checked');
        $.ajax({
            url: '/manage/ticket-status-change/' + ticketId,
            type: 'POST',
            data: {
                'available': available,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            }
        })
    })
});
$('#deleteModal').on('show.bs.modal', function(event) {  
    console.log('modal aberto')
    console.log(event)     
    var button = $(event.relatedTarget) // Botão que acionou o modal
    var ticketId = button.data('ticket-id') // Extrai informações dos atributos data-*
    console.log(ticketId)
    var url = "/manage/ticket-delete/" + ticketId // Constrói a URL para a view de exclusão
    console.log(url)
    $("#confirmDelete").attr('href', url) // Atualiza o link de confirmação de exclusão
})