document.getElementById('send-email-btn').addEventListener('click', function (event) {
    event.preventDefault();

    var responseMessage = document.getElementById('response-message').value;

    var templateParams = {
      to_email: '{{ contact_form.email }}',  
      subject: 'Response to Your Message',
      message: responseMessage
    };

    emailjs.send('gmail', 'template_bxmumuo', templateParams)
      .then(function (response) {
        console.log('SUCCESS!', response.status, response.text);

        alert('Email sent successfully!');  // Exibe um alerta de sucesso

        // Simplesmente muda o status aqui para o que desejar sem AJAX
        document.getElementById('response-message').value = '';  // Limpa o campo de resposta
      }, function (error) {
        console.log('FAILED...', error);
        alert('Failed to send email.');  // Alerta em caso de falha
      });
  });