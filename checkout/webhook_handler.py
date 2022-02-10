from django.http import HttpResponse


class StripeWHHandler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a webhook event"""
        return HttpResponse(
            content=f' Unhandled Webhook received: {event["type"]}',
            status=200)

    def payment_intent_succeeded(self, event):
        """ Handle payment_intent.succeeded webhook"""
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def payment_intent_payment_failed(self, event):
        """ Handle payment_intent.succeeded webhook"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
