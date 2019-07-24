//fonction pour les fenetres modals
$(document).ready(function() {
  $("#button-filtre-membre").click(filtreModal);
  $("#supress-m").click(modalDelete);
  $("#auth-button").click(modalAutorisation)
  $("#myclose,.close,#close-remove,#close-auth").click(()=> {
  $("#corp-filtre,#corp-delete,#corp-auth,#close-auth").addClass("d-none")
     })  
    })
//fonction afficher le modal
const afficher = () => {
  $("#modal-filtre-membre").modal();
}
let cacher_suprimer = () => $("#close-remove").addClass("d-none")

//fonction qui execute tous ce qui conserne l'affichage du filtre et son contenue
var process_filtre = () => {
  afficher() 
  $("#titre-modal").text("Filtre des membres")
  $("#corp-filtre").removeClass('d-none')
  $("#myclose").removeClass('d-none')
  cacher_suprimer()
}
//fonction qui affiche le message de supression
var process_delete = () => {
  afficher() 
  $("#titre-modal").text("Suprimer membre")
  $("#corp-delete,#close-remove").removeClass('d-none')
  $("#myclose").addClass("d-none")
}
//fonction affichage autorisation
var process_autorisation= () => {
  afficher() 
  $("#titre-modal").text("Autorisation modal")
  $("#corp-auth,#close-auth").removeClass('d-none')
  $("#myclose").addClass('d-none')
  cacher_suprimer()
}
var filtreModal = function() {
  try {
       process_filtre()
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

var modalAutorisation = function() {
  try {
       process_autorisation()
  }
  catch (e) {
    alert(e);
  }
}