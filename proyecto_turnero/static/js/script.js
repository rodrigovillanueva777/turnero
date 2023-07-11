$(document).ready(function() {
    $('.toggle-atendido').change(function() {
      var checkbox = $(this);
      var clienteId = checkbox.data('cliente-id');
      var atendido = checkbox.prop('checked');
  
      $.ajax({
        type: 'POST',
        url: '/actualizar-atendido/',
        data: {
          'cliente_id': clienteId,
          'atendido': atendido
        },
        success: function(response) {
          console.log('Valor de atendido actualizado');
        },
        error: function(xhr, textStatus, error) {
          console.log('Error al actualizar el valor de atendido:', error);
        }
      });
    });
  });
  