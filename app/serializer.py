from rest_framework import serializers
from .models import BankMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankMerch
        fields = ('id', 'date', 'description', 'title', 'amount', 'name')