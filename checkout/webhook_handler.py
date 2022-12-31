from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handles the Stripe Web Hook
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles a generic/unknown/unexpected Web Hook event
        """
        return HttpResponse(
            context=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handles the payment intent succeeded WebHook from Stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'WebHook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_failed(self, event):
        """
        Handles the payment intent failed WebHook from Stripe
        """
        return HttpResponse(
            content=f'WebHook received: {event["type"]}',
            status=200
        )
