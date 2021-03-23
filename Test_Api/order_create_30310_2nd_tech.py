import datetime
import json

import requests
from base_data.main_data import MainData
from pages.api import Api_Data
from pages.create_order_locators import Create_Order_Locators, Create_Order_Functions
from pages.instalation_points import Installation_Points, Set_Inatallation_Points_30310


def test_create_order_1(self=None):
    #create customer
    payload = json.dumps(Create_Order_Locators.payload_create_customer_1)  #locator to the customer data
    create = requests.post(url=Create_Order_Functions.url_create_customer(self), data=payload, headers=Api_Data.base_headers )

    customerId = create.json().get('objectId')

    #create_order
    payload = json.dumps(customerId)
    create_order = requests.post(url=Create_Order_Functions.url_create_order(self), data=payload, headers=Api_Data.base_headers)
    orderId = create_order.json().get('objectId')
    #setVehicle
    payload = json.dumps(Create_Order_Locators.payload_set_vehicle)
    set_vehicle = requests.post(url=Create_Order_Functions.url_set_vehicle(self, orderId), data=payload, headers=Api_Data.base_headers)
    set_veh_id = set_vehicle.json().get('objectId')
    set_veh_error = set_vehicle.text

    #setTires
    payload = json.dumps(Create_Order_Locators.payload_set_tires)
    set_tires = requests.post(url=Create_Order_Functions.url_set_tires(self, orderId, vehicleId=set_veh_id), data=payload, headers = Api_Data.base_headers)
    set_tires_id = set_tires.json().get('objectId')
    set_tires_error = set_tires.text

    #create instalation point

    payload = json.dumps(Installation_Points.payload_create_installation_point1_30310)
    create_point = requests.post(url=Create_Order_Functions.url_create_installation_point(self), data=payload, headers = Api_Data.base_headers)
    point_id = create_point.json().get('objectId')
    point_error = create_point.text



    #set installation point
    payload = Set_Inatallation_Points_30310.payload_set_installation_point1_30310(self, instPointObjectId=point_id)
    payload = json.dumps(payload)
    set_installation_point = requests.post(url=Create_Order_Functions.url_set_installation_point(self, orderId=orderId) , data=payload, headers=Api_Data.base_headers)
    set_inst_point_ID = set_installation_point.json().get('objectId')
    status_set_inst_point = set_installation_point.status_code

    #set order service
    #payload = Create_Order_Locators.payload_set_service(self)
    #payload = json.dumps(payload)
    set_service = requests.post(url = Create_Order_Functions.url_set_order_service(self, orderId=orderId, vehicleId=set_veh_id), data= MainData.set_service, headers = Api_Data.base_headers)
    status_set_service = set_service.status_code
    status_set_service_error = set_service.text

    # set Time Slot

    # today = datetime.datetime.now() + datetime.timedelta(days = 1)
    # tomorow_morning = today.strftime('%Y%m%d')
    # fromdate =  datetime.datetime.strptime(tomorow_morning, '%Y%m%d').timestamp()
    # fromdate *= 1000
    # todate = fromdate + 64800000
    # fromdate = 1614168000000
    # todate = 1613403214000
    payload = Create_Order_Functions.payload_set_time_slot(self, fromTime=int(MainData.fromdate), ToTime=int(MainData.todate))
    payload = json.dumps(payload)
    set_time_slot = requests.post(url=Create_Order_Functions.url_set_time_slot(self, orderId=orderId), data=payload, headers=Api_Data.base_headers)
    time_slot_id = set_time_slot.status_code
    time_slot_id_error = set_time_slot.text

    #create_payment

    payload = json.dumps(Create_Order_Locators.payload_create_payment)
    create_payment = requests.post(url=Create_Order_Functions.url_create_payment(self, orderId=orderId), data=payload, headers = Api_Data.base_headers)
    create_payment_status = create_payment.status_code
    create_payment_text = create_payment.text

    return print("CustomerID :", customerId , '\n',
                 "OrderID   :", orderId, '\n',
                 "setVehId  :", set_veh_id, set_veh_error, '\n',
                 "setTiresId : ", set_tires_id, set_tires_error, '\n',
                 "installationPointId : ", point_id,point_error, '\n',
                 "SetInstallationPointId : ", set_inst_point_ID, status_set_inst_point, '\n',
                 "SetService : ", status_set_service, status_set_service_error,  '\n'
                                                                                 "TimeslotId : ", time_slot_id, time_slot_id_error, '\n',
                 "Payment : ", create_payment_status, create_payment_text,
                 end='\n')

def test_create_order_2(self=None):
    #create customer
    payload = json.dumps(Create_Order_Locators.payload_create_customer_2)  #locator to the customer data
    create = requests.post(url=Create_Order_Functions.url_create_customer(self), data=payload, headers=Api_Data.base_headers )
    customerId = create.json().get('objectId')

    #create_order
    payload = json.dumps(customerId)
    create_order = requests.post(url=Create_Order_Functions.url_create_order(self), data=payload, headers=Api_Data.base_headers)
    orderId = create_order.json().get('objectId')
    #setVehicle
    payload = json.dumps(Create_Order_Locators.payload_set_vehicle)
    set_vehicle = requests.post(url=Create_Order_Functions.url_set_vehicle(self, orderId), data=payload, headers=Api_Data.base_headers)
    set_veh_id = set_vehicle.json().get('objectId')

    #setTireste
    payload = json.dumps(Create_Order_Locators.payload_set_tires)
    set_tires = requests.post(url=Create_Order_Functions.url_set_tires(self, orderId, vehicleId=set_veh_id), data=payload, headers = Api_Data.base_headers)
    set_tires_id = set_tires.json().get('objectId')

    #create instalation point

    payload = json.dumps(Installation_Points.payload_create_installation_point2_30310)
    create_point = requests.post(url=Create_Order_Functions.url_create_installation_point(self), data=payload, headers = Api_Data.base_headers)
    point_id = create_point.json().get('objectId')



    #set installation point
    payload = Set_Inatallation_Points_30310.payload_set_installation_point2_30310(self, instPointObjectId=point_id)
    payload = json.dumps(payload)
    set_installation_point = requests.post(url=Create_Order_Functions.url_set_installation_point(self, orderId=orderId) , data=payload, headers=Api_Data.base_headers)
    set_inst_point_ID = set_installation_point.json().get('objectId')
    status_set_inst_point = set_installation_point.status_code

    #set order service
    #payload = Create_Order_Locators.payload_set_service(self)
    #payload = json.dumps(payload)
    set_service = requests.post(url = Create_Order_Functions.url_set_order_service(self, orderId=orderId, vehicleId=set_veh_id), data=MainData.set_service, headers = Api_Data.base_headers)
    status_set_service = set_service.status_code

    # set Time Slot

    # today = datetime.datetime.now() + datetime.timedelta(days = 1)
    # tomorow_morning = today.strftime('%Y%m%d')
    # fromdate =  datetime.datetime.strptime(tomorow_morning, '%Y%m%d').timestamp()
    # fromdate *= 1000
    # todate = fromdate + 64800000
    # fromdate = 1614168000000
    # todate = 1613403214000
    payload = Create_Order_Functions.payload_set_time_slot(self, fromTime=int(MainData.fromdate), ToTime=int(MainData.todate))
    payload = json.dumps(payload)
    set_time_slot = requests.post(url=Create_Order_Functions.url_set_time_slot(self, orderId=orderId), data=payload, headers=Api_Data.base_headers)
    time_slot_id = set_time_slot.status_code

    #create_payment

    payload = json.dumps(Create_Order_Locators.payload_create_payment)
    create_payment = requests.post(url=Create_Order_Functions.url_create_payment(self, orderId=orderId), data=payload, headers = Api_Data.base_headers)
    create_payment_status = create_payment.status_code
    create_payment_text = create_payment.text

    return print("CustomerID :", customerId , '\n',
                 "OrderID   :", orderId, '\n',
                 "setVehId  :", set_veh_id, '\n',
                 "setTiresId : ", set_tires_id, '\n',
                 "installationPointId : ", point_id,'\n',
                 "SetInstallationPointId : ", set_inst_point_ID, status_set_inst_point, '\n',
                 "SetServise :  " , status_set_service, '\n',
                 "TimeslotId : ", time_slot_id,  '\n',
                 "Payment : ", create_payment_status, create_payment_text,
                 end='\n')

def test_create_order_3(self=None):
    #create customer
    payload = json.dumps(Create_Order_Locators.payload_create_customer_3)  #locator to the customer data
    create = requests.post(url=Create_Order_Functions.url_create_customer(self), data=payload, headers=Api_Data.base_headers )
    customerId = create.json().get('objectId')

    #create_order
    payload = json.dumps(customerId)
    create_order = requests.post(url=Create_Order_Functions.url_create_order(self), data=payload, headers=Api_Data.base_headers)
    orderId = create_order.json().get('objectId')
    #setVehicle
    payload = json.dumps(Create_Order_Locators.payload_set_vehicle)
    set_vehicle = requests.post(url=Create_Order_Functions.url_set_vehicle(self, orderId), data=payload, headers=Api_Data.base_headers)
    set_veh_id = set_vehicle.json().get('objectId')

    #setTires
    payload = json.dumps(Create_Order_Locators.payload_set_tires)
    set_tires = requests.post(url=Create_Order_Functions.url_set_tires(self, orderId, vehicleId=set_veh_id), data=payload, headers = Api_Data.base_headers)
    set_tires_id = set_tires.json().get('objectId')

    #create instalation point

    payload = json.dumps(Installation_Points.payload_create_installation_point3_30310)
    create_point = requests.post(url=Create_Order_Functions.url_create_installation_point(self), data=payload, headers = Api_Data.base_headers)
    point_id = create_point.json().get('objectId')



    #set installation point
    payload = Set_Inatallation_Points_30310.payload_set_installation_point3_30310(self, instPointObjectId=point_id)
    payload = json.dumps(payload)
    set_installation_point = requests.post(url=Create_Order_Functions.url_set_installation_point(self, orderId=orderId) , data=payload, headers=Api_Data.base_headers)
    set_inst_point_ID = set_installation_point.json().get('objectId')
    status_set_inst_point = set_installation_point.status_code

    #set order service
    # payload = Create_Order_Locators.payload_set_service(self)
    # payload = json.dumps(payload)
    set_service = requests.post(url = Create_Order_Functions.url_set_order_service(self, orderId=orderId, vehicleId=set_veh_id), data=MainData.set_service, headers = Api_Data.base_headers)
    status_set_service = set_service.status_code

    # set Time Slot

    # today = datetime.datetime.now() + datetime.timedelta(days = 1)
    # tomorow_morning = today.strftime('%Y%m%d')
    # fromdate =  datetime.datetime.strptime(tomorow_morning, '%Y%m%d').timestamp()
    # fromdate *= 1000
    # todate = fromdate + 64800000
    # fromdate = 1614168000000
    # todate = 1613403214000
    payload = Create_Order_Functions.payload_set_time_slot(self, fromTime=int(MainData.fromdate), ToTime=int(MainData.todate))
    payload = json.dumps(payload)
    set_time_slot = requests.post(url=Create_Order_Functions.url_set_time_slot(self, orderId=orderId), data=payload, headers=Api_Data.base_headers)
    time_slot_id = set_time_slot.status_code
    #create_payment

    payload = json.dumps(Create_Order_Locators.payload_create_payment)
    create_payment = requests.post(url=Create_Order_Functions.url_create_payment(self, orderId=orderId), data=payload, headers = Api_Data.base_headers)
    create_payment_status = create_payment.status_code
    create_payment_text = create_payment.text

    return print("CustomerID :", customerId , '\n',
                 "OrderID   :", orderId, '\n',
                 "setVehId  :", set_veh_id, '\n',
                 "setTiresId : ", set_tires_id, '\n',
                 "installationPointId : ", point_id,'\n',
                 "SetInstallationPointId : ", set_inst_point_ID, status_set_inst_point, '\n',
                 "SetServise :  " , status_set_service, '\n',
                 "TimeslotId : ", time_slot_id,  '\n',
                 "Payment : ", create_payment_status, create_payment_text,
                 end='\n')


def test_create_order_4(self=None):
    #create customer
    payload = json.dumps(Create_Order_Locators.payload_create_customer_4)  #locator to the customer data
    create = requests.post(url=Create_Order_Functions.url_create_customer(self), data=payload, headers=Api_Data.base_headers )
    customerId = create.json().get('objectId')

    #create_order
    payload = json.dumps(customerId)
    create_order = requests.post(url=Create_Order_Functions.url_create_order(self), data=payload, headers=Api_Data.base_headers)
    orderId = create_order.json().get('objectId')
    #setVehicle
    payload = json.dumps(Create_Order_Locators.payload_set_vehicle)
    set_vehicle = requests.post(url=Create_Order_Functions.url_set_vehicle(self, orderId), data=payload, headers=Api_Data.base_headers)
    set_veh_id = set_vehicle.json().get('objectId')

    #setTires
    payload = json.dumps(Create_Order_Locators.payload_set_tires)
    set_tires = requests.post(url=Create_Order_Functions.url_set_tires(self, orderId, vehicleId=set_veh_id), data=payload, headers = Api_Data.base_headers)
    set_tires_id = set_tires.json().get('objectId')

    #create instalation point

    payload = json.dumps(Installation_Points.payload_create_installation_point4_30310)
    create_point = requests.post(url=Create_Order_Functions.url_create_installation_point(self), data=payload, headers = Api_Data.base_headers)
    point_id = create_point.json().get('objectId')
    inst_point_error = create_point.text



    #set installation point
    payload = Set_Inatallation_Points_30310.payload_set_installation_point4_30310(self, instPointObjectId=point_id)
    payload = json.dumps(payload)
    set_installation_point = requests.post(url=Create_Order_Functions.url_set_installation_point(self, orderId=orderId) , data=payload, headers=Api_Data.base_headers)
    set_inst_point_ID = set_installation_point.json().get('objectId')
    status_set_inst_point = set_installation_point.status_code

    #set order service
    #payload = Create_Order_Locators.payload_set_service(self)
    #payload = json.dumps(payload)

    set_service = requests.post(url=Create_Order_Functions.url_set_order_service(self, orderId=orderId, vehicleId=set_veh_id), data=MainData.set_service, headers = Api_Data.base_headers)
    status_set_service = set_service.status_code
    set_service_error = set_service.text

    # set Time Slot

    # today = datetime.datetime.now() + datetime.timedelta(days = 1)
    # tomorow_morning = today.strftime('%Y%m%d')
    # fromdate =  datetime.datetime.strptime(tomorow_morning, '%Y%m%d').timestamp()
    # fromdate *= 1000
    # todate = fromdate + 64800000
    # fromdate = 1614168000000
    # todate = 1613403214000
    payload = Create_Order_Functions.payload_set_time_slot(self, fromTime=int(MainData.fromdate), ToTime=int(MainData.todate))
    payload = json.dumps(payload)
    set_time_slot = requests.post(url=Create_Order_Functions.url_set_time_slot(self, orderId=orderId), data=payload, headers=Api_Data.base_headers)
    time_slot_id = set_time_slot.status_code
    time_slot_error = set_time_slot.text

    #create_payment

    payload = json.dumps(Create_Order_Locators.payload_create_payment)
    create_payment = requests.post(url=Create_Order_Functions.url_create_payment(self, orderId=orderId), data=payload, headers = Api_Data.base_headers)
    create_payment_status = create_payment.status_code
    create_payment_text = create_payment.text



    return print("CustomerID :", customerId , '\n',
                 "OrderID   :", orderId, '\n',
                 "setVehId  :", set_veh_id, '\n',
                 "setTiresId : ", set_tires_id, '\n',
                 "installationPointId : ", point_id, inst_point_error, '\n',
                 "SetInstallationPointId : ", set_inst_point_ID, status_set_inst_point, '\n',
                 "SetServise :  " , status_set_service, set_service_error, '\n',
                 "TimeslotId : ", time_slot_id,  time_slot_error, '\n',
                 "Payment : ", create_payment_status,
                 end='\n')
