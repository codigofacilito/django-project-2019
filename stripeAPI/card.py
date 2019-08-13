from . import stripe

def create_card(user, token):
    source = stripe.Customer.create_source(
        user.customer_id,
        source=token
    )

    return source
