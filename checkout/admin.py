from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Add and edit line items in the admin order
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    # These fields are calulated by model methods
    # made readonly so not editable to prevent
    # order details being compromised
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

    # Allows us to specify the order of the fields
    fields = (
        'order_number',
        'date',
        'user_profile',
        'order_total',
        'delivery_cost',
        'grand_total',
        'original_bag',
        'stripe_pid',
        'full_name',
        'email',
        'phone_number',
        'street_address1',
        'street_address2',
        'town_or_city',
        'county',
        'postcode',
        'country',
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
