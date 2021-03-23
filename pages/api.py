import json

import requests

from base_data.base_page import Page
from base_data.main_data import MainData

"""examples"""


class Api_Data():
    payload_create_customer = {"firstName": "1A_Test", "lastName": "A_Test", "email": "autotest@asap.com", "phoneNumber": 8004444444, "reminders": False, "smsNotification": False,
               "zipCode": 30301}
    base_headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
             'user-language': 'en'}





# def api_post():
#         header = {'Accept': 'application/json', 'Content-Type': 'application/json',
#           'user-language': 'en'}
#         url = f"https://{MainData.Place}.backendless.com/api/{MainData.Api}/services/auth/logout"
#         a = requests.post(url,headers=header).status_code
#         return a
#
#
# def api_post_with_payloads():
#     #global a, x
#     a = {}
#     url = f"https://{MainData.Place}.backendless.com/api/{MainData.Api}/services/auth/login"
#     payload = {'email': 'lcmteam@backendless.com', 'password': 'secret'}
#     payload = json.dumps(payload)
#     x = requests.post(url, data=payload, headers={'Accept': 'application/json', 'Content-Type': 'application/json',
#                                                   'user-language': 'en'})
#     #a = x.json()
#     x = x.json().get('user-token')
#     return x





def api_create_customer():
        url = f"{MainData.BaseUrl}/services/customers/"
        payload = {"firstName": "A_Test", "lastName": "A_Test", "email": "autotest@asap.com", "phoneNumber": 8004444444, "reminders": False, "smsNotification": False,
               "zipCode": 30301}
        payload = json.dumps(payload)
        x = requests.post(url, data=payload, headers={'Accept': 'application/json', 'Content-Type': 'application/json',
                                                  'user-language': 'en'})
        a = x.json().get('objectId')
        return a

def url_get_customer(customerId):
    url = f"{MainData.BaseUrl}/services/customers/?customerId={customerId}"
    return url

def api_delete_customer(customerId):
    url = f"{MainData.BaseUrl}/services/customers/"
    header = {'' : '', 'Accept': 'application/json', 'Content-Type': 'application/json', 'user-language': 'en'}


def url_create_customer():
    return f"{MainData.BaseUrl}/services/customers/"

def url_delete_customer():
    return f"{MainData.BaseUrl}/services/customers/"


def payload_update_customer(customerId):
    return {"firstName": "A_Test_update", "lastName": "A_Test_update", "email": "autotest@asap.com", "phoneNumber": 8004444444, "reminders": False, "smsNotification": False,
            "zipCode": 30301, "objectId": customerId}