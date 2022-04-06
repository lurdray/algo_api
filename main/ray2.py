import json
import base64
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction



algod_token = 'ieJBmuXZWA1R89q77eRU6K89OuB3ZRU8bLoJHyM5'
algod_address = 'https://testnet-algorand.api.purestake.io/ps2'
purestake_token = {'X-Api-key': algod_token}

algod_client = algod.AlgodClient(algod_token, algod_address, headers=purestake_token)


def CreateWallet(email):
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))



def GetBalance(wallet_address):
    account_info = algod_client.account_info(wallet_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")



def SendCoin(sender_address, sender_key, receiver_address, amount):
    try:
        params = algod_client.suggested_params()
        params.flat_fee = True
        params.fee = constants.MIN_TXN_FEE 

        note = "Send via Ray API".encode()
        unsigned_txn = transaction.PaymentTxn(sender_address, params, receiver_address, amount, None, note)
        signed_txn = unsigned_txn.sign(sender_key)
        txid = algod_client.send_transaction(signed_txn)
        print("Successfully sent transaction with txID: {}".format(txid))

    except:
        pass





CreateWallet("raymond@gmail.com")
#GetBalance("JWJK6EDFEPR7XVXN7IS7RIDCPGGPCDWJO57I5CELE25DNJLDPWCDQBXZWQ")
#SendCoin("YEBOK7IKDN5ZPRPL5V4EHOSHVBARDLJISE5LQY2LIBFN34GBI4CWQE6PRI", "o74i2p0M/zsdGzWMFLNRJ743hCirKJYxdVLaZHy3vMzBAuV9Cht7l8Xr7XhDukeoQRGtKJE6uGNLQErd8MFHBQ==", "JWJK6EDFEPR7XVXN7IS7RIDCPGGPCDWJO57I5CELE25DNJLDPWCDQBXZWQ", 142580)



