$(document).on('click','.close',function(){
      $("#corp-add,#corp-delete,#close-remove").addClass('d-none')
      $("#monform")[0].reset();
})
$(document).ready(function() {
    $("#button-add-membre").click(addRegionModal);
    $(".update_region").click(updateRegion);
    $(".supress-m").click(modalDelete);
    $("#myclose,#close-remove").click(()=> {
    $("#corp-add,#corp-delete").addClass("d-none")
    $("#monform")[0].reset();
       })  
      })
let title;
      //fonction afficher le modal
const afficher = () => {
    $("#modal-filtre-membre").modal();
  }
  var process_add = (tilte) => {
    afficher() 
    $("#titre-modal").text(title)
    $("#corp-add,#myclose").removeClass('d-none')
    
  }
  var process_delete = () => {
    afficher() 
    $("#titre-modal").text("Suprimer membre")
    $("#corp-delete,#close-remove").removeClass('d-none')
    $("#myclose").addClass("d-none")
  }
  var addRegionModal = function() {
    try {
      title = "Creation nouvelle region"
         process_add(title)
    }
    catch (e) {
      alert(e);
    }
  }
  var updateRegion = function() {
    try {
      title = "Mise a jour region"
      process_add(title)
      $("#name_br").val($(this).data('name_br'))
      $("#name_pr").val($(this).data('name_pr'))
    }
    catch (e) {
      alert(e);
    }
  }
  var modalDelete = function() {
    try {
         process_delete()
    }
    catch (e) {
      alert(e);
    }
  }
  