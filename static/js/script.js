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

// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', function() {
    // Select the button and modal elements
    var showModalButton = document.getElementById('showModalButton');
    var exampleModal = document.getElementById('exampleModal');
    
    // Show the modal when the button is clicked
    if (showModalButton) {
        showModalButton.addEventListener('click', function() {
            var modal = new bootstrap.Modal(alertModal);
            modal.show();
        });
    }

    // Remove the backdrop manually when the modal is hidden
    alertModal.addEventListener('hidden.bs.modal', function () {
        var backdrop = document.querySelector('.modal-backdrop');
        if (backdrop) {
            backdrop.remove();
        }
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const blocks = document.querySelectorAll('.block');
    const slides = document.querySelectorAll('.block-slide');

    function handleScroll() {
        blocks.forEach(block => {
            const rect = block.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom >= 0) {
                if (!block.classList.contains('animated')) {
                    block.classList.add('animated');
                }
            }
        });

        slides.forEach(slide => {
            const rect = slide.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom >= 0) {
                if (!slide.classList.contains('animated')) {
                    slide.classList.add('animated');
                }
            }
        });
    }

    // Add scroll event listener
    window.addEventListener('scroll', handleScroll);
    // Run handleScroll on initial load
    handleScroll();
});


var myCarousel = document.getElementById('carouselExampleCaptions');
  var carousel = new bootstrap.Carousel(myCarousel, {
    interval: 3000,  // Intervalo em milissegundos (3000 ms = 3 segundos)
    ride: 'carousel'
});


