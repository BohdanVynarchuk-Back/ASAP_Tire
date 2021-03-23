import datetime

import datetime as datetime
import time

import ciso8601 as ciso8601
from base_data.main_data import MainData
from base_data.base_page import Page


class Create_Order_Locators():
    payload_create_customer_1 = {"firstName": "Order_Test_1", "lastName": "Order_Test_1", "email": "order1@asap.com", "phoneNumber":8004444444, "reminders": False, "smsNotification": False,
                               "zipCode": 30301}
    payload_create_customer_2 = {"firstName": "Order_Test_2", "lastName": "Order_Test_2", "email": "order2@asap.com", "phoneNumber": 8004444444, "reminders": False, "smsNotification": False,
                                 "zipCode": 30301}
    payload_create_customer_3 = {"firstName": "Order_Test_3", "lastName": "Order_Test_3", "email": "order3@asap.com", "phoneNumber": 8004444444, "reminders": False, "smsNotification": False,
                                 "zipCode": 30301}
    payload_create_customer_4 = {"firstName": "Order_Test_4", "lastName": "Order_Test_4", "email": "order4@asap.com", "phoneNumber": 8004444444, "reminders": False, "smsNotification": False,
                                 "zipCode": 30301}

    payload_set_vehicle = {
        "version": "string",
        "year": "2021",
        "model": {
            "name": "RDX SH-AWD",
            "objectId":"47F1449C-4B3C-483D-A0BA-15DCEC13634F",
            "brand": {
                "objectId":"22BBA393-4CB1-4CD4-A8F9-B8E3A1974330",
                "name": "Acura"
            }
        },
        "tires": {
            "frontTire": {
                "aspectRatio": 0,
                "diameter": 0,
                "price": 0,
                "width": 0
            },
            "rearTire": {
                "aspectRatio": 0,
                "diameter": 0,
                "price": 0,
                "width": 0
            }
        }
    }

    payload_set_tires = {
        "frontTire": {
            "aspectRatio": 0,
            "diameter": 0,
            "price": 0,
            "width": 0
        },
        "rearTire": {
            "aspectRatio": 0,
            "diameter": 0,
            "price": 0,
            "width": 0
        }
    }

    payload_create_installation_point1 = {
        "zipCode": 30310,
        "address": "1197 Avon Ave SW",
        "additionalInformation": "info1",
        "aptOrSuit": "1",
        "city": "Atlanta",
        "locationType": "home",
        "state": "GA",
        "coordinates": {}
    }
    payload_create_installation_point2 = {
        "zipCode": 30310,
        "address": "1288 Lorenzo Dr SW",
        "additionalInformation": "info1",
        "aptOrSuit": "1",
        "city": "Atlanta",
        "locationType": "home",
        "state": "GA",
        "coordinates": {}
    }
    payload_create_installation_point3 = {
        "zipCode": 30310,
        "address": "1717 Lee St SW",
        "additionalInformation": "info1",
        "aptOrSuit": "1",
        "city": "Atlanta",
        "locationType": "home",
        "state": "GA",
        "coordinates": {}
    }

    payload_create_installation_point4 = {
        "zipCode": 30310,
        "address": "902 Pinehurst Terrace SW",
        "additionalInformation": "info1",
        "aptOrSuit": "1",
        "city": "Atlanta",
        "locationType": "home",
        "state": "GA",
        "coordinates": {}
    }



    payload_create_payment = {
        "number": "4111111111111111",
        "expirationDate": "02/2025",
        "cvv": "123"
    }

    payload_set_service = '["175597D5-DDFB-4EA5-A81F-84898E3490F6"]'





class Create_Order_Functions(Page):
    def url_create_customer(self):
        return f"{MainData.BaseUrl}/services/customers/"


    def url_create_order(self):
        return f"{MainData.BaseUrl}/services/orders/"

    def url_set_vehicle(self, orderid):
        return f"{MainData.BaseUrl}/services/orders/{orderid}/vehicles"

    def url_set_tires(self, orderid, vehicleId):
        return f"{MainData.BaseUrl}/services/orders/{orderid}/vehicles/{vehicleId}/tires"

    def url_create_installation_point(self):
        return f"{MainData.BaseUrl}/services/installation_point/"

    def payload_set_installation_point1(self, instPointObjectId):
       return {
    "zipCode": 30310,
    "address": "1197 Avon Ave SW",
    "additionalInformation": "info1",
    "aptOrSuit": "1",
    "city": "",
    "locationType": "home",
    "state": "GA",
    "coordinates": {},
    "objectId" : f'{instPointObjectId}'
    }

    def url_set_installation_point(self, orderId):
        return f"{MainData.BaseUrl}/services/orders/{orderId}/installation-point"


    def url_set_time_slot(self, orderId):
        return f"{MainData.BaseUrl}/services/orders/{orderId}/time-slot"

    def payload_set_time_slot(self, fromTime, ToTime):
        return {
            "type": "afternoon",
            "fromTime": int(f'{fromTime}'),
            "toTime": int(f'{ToTime}')

        }

    def url_create_payment(self, orderId):
        return f"{MainData.BaseUrl}/services/orders/{orderId}/payment-method"


    def url_set_order_service(self, orderId, vehicleId):
        return f"{MainData.BaseUrl}/services/orders/{orderId}/vehicles/{vehicleId}/order-services"

