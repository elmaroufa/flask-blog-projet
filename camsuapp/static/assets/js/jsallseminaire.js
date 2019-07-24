$(document).on('click','.close',function(){
    $("#corp-delete").addClass('d-none')
    
})

$(document).ready(function(){
    $("#supress-m").click(modalDelete);
})

const afficher = () => {
    $("#modal-filtre-membre").modal();
  }

  var process_delete = () => {
    afficher() 
    $("#titre-modal").text("Suprimer membre")
    $("#corp-delete,#close-remove").removeClass('d-none')
    $("#myclose").addClass("d-none")
  }

  var modalDelete = function() {
    try {
         process_delete()
    }
    catch (e) {
      alert(e);
    }
  }