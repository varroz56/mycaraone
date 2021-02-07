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

// Handle form submit
// create form variable to handle events on it
var form = document.getElementById("payment-form");
// if the submit buttion clicked
form.addEventListener("submit", function (ev) {
  ev.preventDefault();

  card.update({ disabled: true });
  $("#submit-button").attr("disabled", true);
  $("#payment-form").fadeToggle("slow");
  $("#loading-overlay").fadeToggle(70);
  // check card payment
  // with the form details
  stripe
    .confirmCardPayment(client_secret, {
      payment_method: {
        card: card,
        billing_details: {
          name: $.trim(form.full_name.value),
          phone: $.trim(form.phone_number.value),
          email: $.trim(form.email.value),
          address: {
            line1: $.trim(form.street_number.value),
            line2: $.trim(form.route.value),
            city: $.trim(form.locality.value),
            country: $.trim(form.country.value),
          },
        },
      },
    })
    // if the payment did not go through
    // error message with icon again
    .then(function (result) {
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
        // if the payment confirmed, the form can be submitted
        if (result.paymentIntent.status === "succeeded") {
          form.submit();
        }
      }
    });
});
