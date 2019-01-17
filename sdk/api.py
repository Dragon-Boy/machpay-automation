import requests
import credential


#
# Base url and request header
#


ROOT_URL = 'https://sandbox.api.machpay.com/v1/'
HEADER = {
    'X-Client-Id': credential.ClientID,
    'X-Client-Secret': credential.ClientSecret,
    'Content-Type': 'application/json'
}


#
# Sender
#

# Creates sender on the system

def save_sender(body):

    response = requests.post(ROOT_URL + "senders/", headers=HEADER, json=body)
    return response
