// https://stripe.com/docs/stripe-js
// pull stripe api keys from the checkout page
var stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1);
var client_secret = $("#id_client_secret").text().slice(1, -1);
var found_billing_address = $("#id_found_billing_address").text().slice(1, -1);
console.log(found_billing_address);
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
var card = elements.create("card", { hidePostalCode : true, style: style });
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

// Handle form submit
// create form variable to handle events on it
var form = document.getElementById("payment-form");
// if the submit buttion clicked
form.addEventListener("submit", function (ev) {
  // disable card update, form fade out, start the spinner
  ev.preventDefault();
  card.update({ disabled: true });
  $("#submit-button").attr("disabled", true);
  $("#payment-form").fadeToggle("slow");
  $("#loading-overlay").fadeToggle(70);

  if (found_billing_address){
    var name = $.trim(form.full_name.value);
    var phone = $.trim(form.phone_number.value);
    var email = $.trim(form.email.value);
    var line1 = $.trim(form.street_number.value);
    var line2 = $.trim(form.route.value);
    var city = $.trim(form.locality.value);
    var country = $.trim(form.country.value);
  }
  else{
    var name = getElementById(full_name).value;
    var phone = getElementById(phone_number).value;
    var email = getElementById(email).value;
    var line1 = getElementById(street_number).value;
    var line2 = getElementById(route).value;
    var city = getElementById(locality).value;
    var country = getElementById(country).value;

  }
  console.log(name);
  //using the csrf token
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  console.log(csrfToken);
  // define postData form the csrf token and the client secret
  var postData = {
    csrfmiddlewaretoken: csrfToken,
    client_secret: client_secret,
  };
  //define url for the post
  var url = "/checkout/cache_checkout_data/";
  // post data and awaitng for confirmation, that the intent was updated successfully
  $.post(url, postData)
    .done(function () {
      //stripe confirm payment metyhod adding billing address
      stripe
        .confirmCardPayment(client_secret, {
          payment_method: {
            card: card,
            billing_details: {
              name: name,
              phone: phone,
              email: email,
              address: {
                line1: line1,
                line2: line2,
                city: locality,
                country: country,
              },
            },
          },
        })
        .then(function (result) {
          // if there is any issue
          if (result.error) {
            var errorDiv = document.getElementById("card-errors");
            var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-exclamation-triangle"></i>
                    </span>
                    <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $("#payment-form").fadeToggle(100);
            $("#loading-overlay").fadeToggle(100);
            card.update({ disabled: false });
            $("#submit-button").attr("disabled", false);
          } else {
            // the payment was successful, the form can be submitted
            if (result.paymentIntent.status === "succeeded") {
              form.submit();
            }
          }
        });
    })
    .fail(function () {
      //if the post fails reload the page
      location.reload();
    });
});