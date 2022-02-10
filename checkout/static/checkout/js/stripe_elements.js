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
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
      'csrfmiddlewaretoken': csrfToken,
      'client_secret': clientSecret,
      'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    //Once data is posted Stripe confims payment
    $.post(url, postData).done(function() {

      stripe.confirmCardPayment(clientSecret, {
        payment_method: {
          card: card,
          billing_details: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            email: $.trim(form.email.value),
            address:{
              line1: $.trim(form.street_address1.value),
              line2: $.trim(form.street_address2.value),
              city: $.trim(form.town_or_city.value),
              country: $.trim(form.country.value),
              state: $.trim(form.county.value),
            }
          }
        },
        shipping: {
              name: $.trim(form.full_name.value),
              phone: $.trim(form.phone_number.value),
              email: $.trim(form.email.value),
              address:{
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                state: $.trim(form.county.value),
              }
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
    }).fail(function() {
      // reloads the page and displays error in django messages
      location.reload();
    })
});