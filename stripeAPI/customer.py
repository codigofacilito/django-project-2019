from . import stripe

def create_customer(user):
    customer = stripe.Customer.create(
        description=user.description
    )

    return customer
