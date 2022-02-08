/*
main stripe payment flow comes from here:
https://stripe.com/docs/js
*/


var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey, {
    locale: 'en'
});
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

card.on('change', function(event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
      displayError.textContent = event.error.message;
    } else {
      displayError.textContent = '';
    }
  });

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true)
    stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    },
  }).then(function(result) {
      if (result.error) {
          displayError.textContent = result.error.message;
          card.update({'disabled': false});
          $('#submit-button').attr('disabled', false)
      } else {
        if (result.paymentIntent.status === 'succeeded') {
            form.submit();
        }
      }
  });
});