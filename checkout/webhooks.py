from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listens for the Stripe WebHooks
    """
    # Stripe Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # get WebHook data & verify signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(content=e, status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up WebHook Handler
    handler = StripeWH_Handler(request)

    # Map WebHook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': (
            handler.handle_payment_intent_failed),
    }

    # Get WebHook event type from Stripe
    event_type = event['type']

    # If a handler exists for the event, get it from the event map
    # Use generic one as default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
