import time
import json

import requests
from base_data.base_page import Page
from pages.api import api_create_customer, Api_Data, url_create_customer, url_delete_customer, \
    url_get_customer, payload_update_customer
from pages.home_page import HomePage

customerId = ""

def test_create_customer_api():
    global customerId
    payload = json.dumps(Api_Data.payload_create_customer)
    create = requests.post(url=url_create_customer(), data=payload, headers=Api_Data.base_headers )
    customerId = create.json().get('objectId')

##  Create Asserts
    status_code_check= create.status_code
    first_name_check = create.json().get('firstName')
    last_name_check = create.json().get('lastName')
    email_check = create.json().get('email')
    phoneNumber_check = create.json().get('phoneNumber')
    zipCode_check = create.json().get('zipCode')

##  Get Asserts
    get_user  = requests.get(url=url_get_customer(customerId=customerId), data = payload)
    get_status_code_check = get_user.status_code
    get_first_name_check = get_user.json().get('firstName')
    get_last_name_check = get_user.json().get('lastName')
    get_email_check = get_user.json().get('email')
    get_phoneNumber_check = get_user.json().get('phoneNumber')
    get_zipCode_check = get_user.json().get('zipCode')
    get_customerId = get_user.json().get('objectId')

## Post condtion
    payload = json.dumps(customerId)
    delete = requests.delete(url= url_delete_customer(), data= payload)
    delete_result = delete.status_code
    assert delete_result == 200

##  Asserts
    assert  status_code_check == 200
    assert first_name_check == Api_Data.payload_create_customer['firstName']
    assert last_name_check == Api_Data.payload_create_customer['lastName']
    assert email_check == Api_Data.payload_create_customer['email']
    assert int(phoneNumber_check) == Api_Data.payload_create_customer['phoneNumber']
    assert int(zipCode_check) == Api_Data.payload_create_customer['zipCode']

    assert get_status_code_check == 200
    assert get_first_name_check == Api_Data.payload_create_customer['firstName']
    assert get_last_name_check == Api_Data.payload_create_customer['lastName']
    assert get_email_check == Api_Data.payload_create_customer['email']
    assert int(get_phoneNumber_check) == Api_Data.payload_create_customer['phoneNumber']
    assert int(get_zipCode_check) == Api_Data.payload_create_customer['zipCode']
    assert get_customerId == customerId



def test_delete_customer_api():
    global customerId
    ## Precondition to create customer
    payload = json.dumps(Api_Data.payload_create_customer)
    create = requests.post(url=url_create_customer(), data=payload, headers=Api_Data.base_headers )
    customerId = create.json().get('objectId')

    ## Delete customer
    payload = json.dumps(customerId)
    delete = requests.delete(url= url_delete_customer(), data= payload)
    ##  Asserts
    assert delete.status_code == 200
#TODO add get request



def test_update_customer_api():
# Precondition - create customer
    payload = json.dumps(Api_Data.payload_create_customer)
    create = requests.post(url=url_create_customer(), data=payload, headers=Api_Data.base_headers )
    customerId = create.json().get('objectId')
# update customer
    update = requests.put(url=url_create_customer(), data= json.dumps(payload_update_customer(customerId)), headers=Api_Data.base_headers )
#get asserts
    status_code_check= update.status_code
    first_name_check = update.json().get('firstName')
    last_name_check = update.json().get('lastName')
    email_check = update.json().get('email')
    phoneNumber_check = update.json().get('phoneNumber')
    zipCode_check = update.json().get('zipCode')
    customerId_check = update.json().get('objectId')
#Postcondition - Delete customer
    payload = json.dumps(customerId)
    delete = requests.delete(url=url_delete_customer(), data=payload)
#Asserts
    assert  status_code_check == 200
    assert first_name_check == payload_update_customer(customerId)['firstName']
    assert last_name_check == payload_update_customer(customerId)['lastName']
    assert email_check == payload_update_customer(customerId)['email']
    assert int(phoneNumber_check) == payload_update_customer(customerId)['phoneNumber']
    assert int(zipCode_check) == payload_update_customer(customerId)['zipCode']
    assert customerId_check == customerId
    assert delete.status_code == 200



