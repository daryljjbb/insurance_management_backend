# core/serializers.py
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Customer,Policy




class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"

    
class PolicySerializer(serializers.ModelSerializer):

    customer_name = serializers.CharField(
        source="customer.name",
        read_only=True
    )

    class Meta:
        model = Policy
        fields = ['id', 'customer', 'policy_number', 'policy_type', 'effective_date', 'expiration_date', 'premium_amount', 'customer_name']
        read_only_fields = ['user']