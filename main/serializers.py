from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import *



class WalletSerializer(serializers.Serializer):
    address = serializers.CharField(max_length="120")
    private_key = serializers.CharField(max_length="120")

    passphrase0 = serializers.CharField(max_length="30")
    passphrase1 = serializers.CharField(max_length="30")
    passphrase2 = serializers.CharField(max_length="30")
    passphrase3 = serializers.CharField(max_length="30")
    passphrase4 = serializers.CharField(max_length="30")
    passphrase5 = serializers.CharField(max_length="30")
    passphrase6 = serializers.CharField(max_length="30")
    passphrase7 = serializers.CharField(max_length="30")
    passphrase8 = serializers.CharField(max_length="30")
    passphrase9 = serializers.CharField(max_length="30")
    passphrase10 = serializers.CharField(max_length="30")
    passphrase11 = serializers.CharField(max_length="30")
    
    class Meta:
        #model = Wallet
        # fields = ('id', 'title', 'description', 'completed')
        # Shortcut for getting all fields
        fields = ('address', 'private_key', 'passphrase0', 'passphrase1', 'passphrase2', 'passphrase3',
            'passphrase4', 'passphrase5', 'passphrase6', 'passphrase7', 'passphrase8', 'passphrase9', 'passphrase10',
            'passphrase11')



class BalanceSerializer(serializers.Serializer):
    balance = serializers.CharField(max_length=120)
    class Meta:
        #model = Wallet
        fields = ('balance')



class TxnSerializer(serializers.Serializer):
    tx_hash = serializers.CharField(max_length=120)
    class Meta:
        #model = Wallet
        fields = ('tx_hash')
