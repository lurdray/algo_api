from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
from .ray import *


import json
import base64
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction




@api_view(['POST'])
def WalletView(request):

    if request.method == 'POST':
        email = request.data["email"]

        wallet = CreateWallet(email)


        data = {

        "address": wallet["address"],
        "private_key": wallet["private_key"],
        "passphrase0": wallet["passphrase0"],
        "passphrase1": wallet["passphrase1"],
        "passphrase2": wallet["passphrase2"],
        "passphrase3": wallet["passphrase3"],
        "passphrase4": wallet["passphrase4"],
        "passphrase5": wallet["passphrase5"],
        "passphrase6": wallet["passphrase6"],
        "passphrase7": wallet["passphrase7"],
        "passphrase8": wallet["passphrase8"],
        "passphrase9": wallet["passphrase9"],
        "passphrase10": wallet["passphrase10"],
        "passphrase11": wallet["passphrase11"],

        }


        return Response(data)



@api_view(['GET'])
def GetBalanceView(request, wallet_address):

    if request.method == 'GET':
        balance = GetBalance(wallet_address)

        data = {
        "balance": str(balance),
        }

        return Response(data)

       








@api_view(['POST'])
def SendCoin(request):

    if request.method == 'POST':
        sender_address = request.data["sender_address"]
        sender_key = request.data["sender_key"]
        receiver_address = request.data["receiver_address"]
        amount = request.data["amount"]

        txn_hash = SendCoin(sender_address, sender_key, receiver_address, amount)

        data = {
        "txn_hash": str(txn_hash),

        }

        return Response(data)



