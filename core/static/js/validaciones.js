$(function(){
  $("#formulariocliente").validate({
       rules: {
              nomCli:"required",
              apeCli: "required",
              correoCli:{ required: true,
                email:true},
              fonoCli: "required",
              direccionCli:"required"
              
          }, //rules
      messages: {
          nomCli: {
              required: 'Ingresa un nombre'
          },
          apeCli: {
              required: 'Ingresa un apellido',                
          },
          correoCli:{
              required: 'Ingrese un correo electronico',
              email:'Formato de correo no valido'
          },
          fonoCli:{
              required: 'Ingrese un telefono',
          },
          direccionCli: {
              required: 'Ingrese una direccion',
              }
      }
  }); 
}); 
$(function(){
    $("#formulariomodicliente").validate({
        rules: {
                nomCli:"required",
                apeCli: "required",
                correoCli:{ required: true,
                email:true},
                fonoCli: "required",
                direccionCli:"required"
                
            }, //rules
        messages: {
            nomCli: {
                required: 'Ingresa un nombre'
            },
            apeCli: {
                required: 'Ingresa un apellido',                
            },
            correoCli:{
                required: 'Ingrese un correo electronico',
                email:'Formato de correo no valido'
            },
            fonoCli:{
                required: 'Ingrese un telefono',
            },
            direccionCli: {
                required: 'Ingrese una direccion',
                }
        }
    }); 
}); 
