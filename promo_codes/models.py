import string
import random

from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save

class PromoCodeManager(models.Manager):

    def get_valid(self, code):
        now = timezone.now()

        return self.filter(code=code).filter(used=False).filter(valid_from__lte=now).filter(valid_to__gte=now).first()

class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.FloatField(default=0.0)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = PromoCodeManager()

    def __str__(self):
        return self.code

    def use(self):
        #self.used = True
        self.save()

def set_code(sender, instance, *args, **kwargs):
    if instance.code:
        return

    chars = string.ascii_uppercase + string.digits
    instance.code = ''.join( random.choice(chars) for _ in range(10) )

pre_save.connect(set_code, sender=PromoCode)
