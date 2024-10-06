console.log('Script carregado corretamente');
/* 
 * Inspired by "HerBody"  available at https://github.com/michmattera/HerBody. 
 * This work guided the implementation of to display autotmatic all the alerts generate in the project.
 */

document.addEventListener('DOMContentLoaded', function() {
    var alertNode = document.querySelector('.alert');
    if (alertNode) {
        var alert = new bootstrap.Alert(alertNode);
        
        // Set a timeout to close the alert after 3 seconds (3000 ms)
        setTimeout(function() {
            alert.close();
        }, 3000);  // Change the value 3000 to the desired time in milliseconds
    }
});

// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', function() {
    var showModalButton = document.getElementById('showModalButton');
    var exampleModal = document.getElementById('loginPromptModal');

    if (showModalButton) {
        showModalButton.addEventListener('click', function() {
            var modal = new bootstrap.Modal(exampleModal);
            modal.show();
        });
    }
    document.addEventListener('DOMContentLoaded', function() {
        var showInvalidCouponModal = document.body.dataset.showInvalidCouponModal === "true";
        var invalidCouponModal = document.getElementById('invalidCouponModal');
    
        if (showInvalidCouponModal && invalidCouponModal) {
            var modal = new bootstrap.Modal(invalidCouponModal);
            modal.show();
        }
    });
  

    // Add a listener for when the modal is hidden
    exampleModal.addEventListener('hidden.bs.modal', function () {
        var backdrop = document.querySelector('.modal-backdrop');
        if (backdrop) {
            backdrop.remove();
        }
        // Remove 'modal-open' class from <body> if it exists
        document.body.classList.remove('modal-open');
        console.log('Modal closed and backdrop removed.');
    });
});

/* 
 * Inspired by Youtube Tutorial, available at https://www.youtube.com/watch?v=0TnO1GzKWPc. 
 * This work guided the implementation of scroll animation. 
 */

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


