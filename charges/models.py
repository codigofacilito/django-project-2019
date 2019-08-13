from django.db import models

from users.models import User
from orders.models import Order

from stripeAPI.charge import create_charge as create_charge_stripe

class ChargeManager(models.Manager):

    def create_charge(self, order):
        charge = create_charge_stripe(order)

        return self.create(user=order.user,
                            order=order,
                            charge_id=charge.id,
                            amount=charge.amount,
                            payment_method=charge.payment_method,
                            status=charge.status)

class Charge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    charge_id = models.CharField(max_length=50)
    amount = models.IntegerField()#Centavos
    payment_method = models.CharField(max_length=50) #id
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ChargeManager()

    def __str__(self):
        return self.charge_id
