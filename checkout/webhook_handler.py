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
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # clean data from shipping details to prevent empty strings in db
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        order = Order.objects.get(
            full_name__iexact=shipping_details.name,
            email__iexact=billing_details.email,
            phone_number__iexact=shipping_details.phone,
            country__iexact=shipping_details.address.country,
            postcode__iexact=shipping_details.address.postal_code,
            town_or_city__iexact=shipping_details.address.city,
            street_address1__iexact=shipping_details.address.line1,
            street_address2__iexact=shipping_details.address.line2,
            county__iexact=shipping_details.address.state,
            grand_total=grand_total,
        )
        order_exists = True
        return HttpResponse(
                    content=f'WebHook received: {event["type"]} | SUCCESS: Verified order already in database',
                    status=200
                )
        except Order.DoesNotExist:
            try:
                for item_id, quantity in json.loads(bag).items():
                    order = Order.objects.create(
                        full_name=shipping_details.name,
                        email=billing_details.email,
                        phone_numbert=shipping_details.phone,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.address.state,
                    )
                    product = Product.objects.get(id=item_id)
                    if isinstance(quantity, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
            except Exeception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'WebHook received: {event["type"]} | ERROR: {e}',
                    status=500
                )
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
