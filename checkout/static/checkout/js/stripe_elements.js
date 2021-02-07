// https://stripe.com/docs/stripe-js
// pull stripe api keys from the checkout page
var stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1);
var client_secret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
// stile the card element
var style = {
  base: {
    color: "#000",
    fontFamily: '"Yusei Magic", sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};
// create the card element
var card = elements.create("card", { hidePostalCode: true, style: style });
// mount on page load
card.mount("#card-element");

// handle errors on card element

card.addEventListener("change", function (event) {
  var errorDiv = document.getElementById("card-errors");
  // the error present with an icon and the message
  // the target div is supplied by stripe
  if (event.error) {
    var html = `
          <span class="icon" role="alert">
            <i class="fas fa-exclamation-triangle"></i>
          </span>
          <span>${event.error.message}</span>
      `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = "";
  }
});

// get the form object by id
var form = document.getElementById('payment-form');
// awaitng to submit the form
form.addEventListener('submit', function(ev) {
  // disable card update, form fade out, start the spinner
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(slow);
    $('#loading-overlay').fadeToggle(70);
 
 
    // using the csrf token
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // define postData form the csrf token and the client secret
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
    };
    //define url for the post
    var url = '/checkout/cache_checkout_data/';
    // post data and awaitng for confirmation, that the intent was updated successfully
    $.post(url, postData).done(function () {
      //stripe confirm payment metyhod adding billing address
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_number.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.locality.value),
                        state:"",
                    }
                }
            },
        }).then(function(result) {
            // if there is any issue
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-exclamation-triangle"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
              // the payment was successful, the form can be submitted
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        //if the post fails reload the page
        location.reload();
    })
});