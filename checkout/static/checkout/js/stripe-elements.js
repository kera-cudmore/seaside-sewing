/*  Core logic/payment flow for this comes from here:
    https://stripe.com/docs/js
    https://stripe.com/docs/payments/accept-a-payment	
    CSS from here:
    https://stripe.com/docs/stripe-js 
*/

// We are slicing the first and last characters to remove the " " around the key
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
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
        color: '#A82114',
        iconColor: '#A82114'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');


