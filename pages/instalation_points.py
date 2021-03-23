class Installation_Points():
    a = ""
    payload_create_installation_point1_30310 = {
        "zipCode": 30518,
        "address": "4550 S Lee St",
        "additionalInformation": "info1",
        "aptOrSuit": "1",
        "city": "Buford",
        "locationType": "home",
        "state": "GA",
        "coordinates": {}
    }
    #4550 S Lee St, Buford, GA 30518, Соединенные Штаты
    payload_create_installation_point2_30310 = {
        "zipCode": 30040,
        "address": "501 Lakeland Plaza",
        "additionalInformation": "info1",
        "aptOrSuit": "1",
        "city": "Cumming",
        "locationType": "home",
        "state": "GA",
        "coordinates": {}
    }

    payload_create_installation_point3_30310 = {
        "zipCode": 30041,
        "address": "1614 Peachtree Pkwy",
        "additionalInformation": "info1",
        "aptOrSuit": "1",
        "city": "Cumming",
        "locationType": "home",
        "state": "GA",
        "coordinates": {}
    }
    #1614 Peachtree Pkwy, Cumming, GA 30041, Соединенные Штаты
    payload_create_installation_point4_30310 = {
        "zipCode": 30024,
        "address": "2609 Peachtree Pkwy B",
        "additionalInformation": "info1",
        "aptOrSuit": "1",
        "city": "Suwanee",
        "locationType": "home",
        "state": "GA",
        "coordinates": {}
    }
    #2609 Peachtree Pkwy B, Suwanee, GA 30024, Соединенные Штаты

class Set_Inatallation_Points_30310():
    def payload_set_installation_point1_30310(self, instPointObjectId):
        return {
            "zipCode": 30518,
            "address": "4550 S Lee St",
            "additionalInformation": "info1",
            "aptOrSuit": "1",
            "city": "Buford",
            "locationType": "home",
            "state": "GA",
            "coordinates": {},
            "objectId" : f'{instPointObjectId}'
        }

    def payload_set_installation_point2_30310(self, instPointObjectId):
        return {
            "zipCode": 30040,
            "address": "501 Lakeland Plaza",
            "additionalInformation": "info1",
            "aptOrSuit": "1",
            "city": "Cumming",
            "locationType": "home",
            "state": "GA",
            "coordinates": {},
            "objectId" : f'{instPointObjectId}'
        }
    def payload_set_installation_point3_30310(self, instPointObjectId):
        return {
            "zipCode": 30041,
            "address": "1614 Peachtree Pkwy",
            "additionalInformation": "info1",
            "aptOrSuit": "1",
            "city": "Cumming",
            "locationType": "home",
            "state": "GA",
            "coordinates": {},
            "objectId" : f'{instPointObjectId}'
        }
    def payload_set_installation_point4_30310(self, instPointObjectId):
        return {
            "zipCode": 30024,
            "address": "2609 Peachtree Pkwy B",
            "additionalInformation": "info1",
            "aptOrSuit": "1",
            "city": "Suwanee",
            "locationType": "home",
            "state": "GA",
            "coordinates": {},
            "objectId" : f'{instPointObjectId}'
        }