from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handles the Stripe Web Hook
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles the Web Hook event
        """
        return HttpResponse(
            context=f'Webhook received: {event["type"]}',
            status=200
        )
