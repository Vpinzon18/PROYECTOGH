const btnEliminacion=document.querySelectorAll('.btnEliminacion')


(function () {
    
    btnEliminacion.array.forEach(btn => {
        btn.addEventListener('click',function(e){
            let confirmacion=confirm("¿Confirma la eliminacion del Usuario?");
            if (!confirmacion){
                e.preventDefault();
            }
        })
        
    });
})



