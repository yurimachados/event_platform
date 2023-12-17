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
            },
            success: function(response){
                if(response.status == 'success'){
                    showMessage(response.message);
   
                }
            }
        })
    })
    $('#deleteModal').on('show.bs.modal', function(event) {     
        var button = $(event.relatedTarget) // Botão que acionou o modal
        var ticketId = button.data('ticket-id') // Extrai informações dos atributos data-*
        var url = "/manage/ticket-delete/" + ticketId // Constrói a URL para a view de exclusão
        $("#confirmDelete").attr('href', url) // Atualiza o link de confirmação de exclusão
    })

    // Função para exibir mensagens recebidas via ajax
    function showMessage(message){

        $('.MessageToast').remove()

        let messageToast = "<div id='AjaxMessageToast'class='MessageToast message-success' role='alert' aria-live='assertive' aria-atomic='true'><div class='toast-header'><strong class='mr-auto'>Event Hub</strong><button type='button' class='ml-2 mb-1 close' data-dismiss='toast' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div><div class='toast-body'><p>" + message + "</p></div></div>"

        $('.main-container').prepend(messageToast);

        $('#AjaxMessageToast .close').on('click', function(){
            $('#AjaxMessageToast').remove();
        })
    }

});