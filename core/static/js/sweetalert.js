function alerta(event) {
    event.preventDefault();
    const link = event.target.href
    alertaDoce(link);
}

function alertaDoce(link) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-danger',
            cancelButton: 'btn btn-success'
        },
        buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
        title: 'Você tem certeza??',
        text: "Você não poderá reverter isso!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sim, deletar!',
        cancelButtonText: 'Não, cancelar!',
        reverseButtons: true
    }).then((result) => {
        if (result.isConfirmed) {
            swalWithBootstrapButtons.fire(
                'Deletado!',
                'Removido!',
                'success'
            );

            setTimeout(() => {
                window.location.href = link
            }, 1000);

        } else if (
            result.dismiss === Swal.DismissReason.cancel
        ) {
            swalWithBootstrapButtons.fire(
                'Cancelado',
                'Sua música está segura :)',
                'error'
            );
        }
    })
}