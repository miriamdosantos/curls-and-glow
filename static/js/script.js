console.log('Script carregado corretamente');

document.addEventListener('DOMContentLoaded', function() {
    var alertNode = document.querySelector('.alert');
    if (alertNode) {
        var alert = new bootstrap.Alert(alertNode);
        
        // Set a timeout to close the alert after 3 seconds (3000 ms)
        setTimeout(function() {
            alert.close();
        }, 2000);  // Change the value 3000 to the desired time in milliseconds
    }
});


