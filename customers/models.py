# core/models.py
from django.db import models
from django.conf import settings


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    # New fields
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)


    # This links the invoice to a specific user
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="customers",
        null=True, # Allow existing ones to be null for now
        blank=True
    )

    def __str__(self):
        return self.name
    

class Policy(models.Model):

    POLICY_TYPE = [
        ("auto", "Auto"),
        ("home", "Home"),
        ("life", "Life"),
    ]
    customer = models.ForeignKey(
        Customer,
        related_name="policies",
        on_delete=models.CASCADE
    )
    policy_number = models.CharField(max_length=255)
    policy_type = models.CharField(
        max_length=20,
        choices=POLICY_TYPE,
        default="auto"
    )
    effective_date = models.DateField()
    expiration_date = models.DateField()
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # This links the invoice to a specific user
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="policies",
        null=True, # Allow existing ones to be null for now
        blank=True
    )

    def __str__(self):
        return self.name