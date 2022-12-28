from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Allows us to add and edit line items in the admin
    right from inside the order model, this will show
    editable items on the order page
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    # These fields are calulated by model methods so we don't want
    # anyone to have the ability to edit them as it could
    # compromise the integrety of an order
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
    )

    # Not 100% necessary - but will allow us to specify the order of the
    # fields in the admin interface which would otherwise be adjusted
    # by Django due to use using some readonly fields -
    # this allows us to keep the order the same as in the model
    fields = (
        'order_number',
        'date',
        'full_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
    )

    # This restricts the columns that show up in the order list tox
    # only a few key items
    list_display = (
        'order_number',
        'date',
        'full_name',
        'order_total',
        'delivery_cost',
        'grand_total',
    )

    # orders them by date in reverse chronological order (most recent
    # at the top)
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
