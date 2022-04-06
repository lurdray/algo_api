from django.urls import path
from . import views

app_name = "main"


from . import views
from rest_framework import routers
from django.urls import path, include


urlpatterns = [


    #crypto api
    path('create-wallet/', views.WalletView),
    path('get-balance/<str:wallet_address>/', views.GetBalanceView),
    path('send-coin/', views.SendCoin),

    #get balance
    #send bnb
    #send bep




]

