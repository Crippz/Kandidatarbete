import json
import datetime
import requests

APIServer = 'https://test4.oamportal.com' 
access_token = None
 
#Retrieve access token (authentication)
def createToken():
    print("createToken")
    client_id = 'chalmers_test'
    client_secret = 'oWN3hmv9K6kYSGF96IP3pfWzrnk12Vo7'
    url = APIServer + "/oauth2/token"
    data = {
        'grant_type': 'client_credentials',
        'scope':'chargeportalservices'
    }

    response = requests.post(url, data=data, auth=(client_id,client_secret))
    #print(response.text)                           #debugging
    print(response)                                #debugging
    acc_response_json = response.json()             #Convert response to json object
    acc_token = acc_response_json["access_token"]   #Get the access token from the json object
    return(acc_token)

#Start Charger
def startCharger(token):
    print("startCharger")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    data = '{"evseId":"d4ceb292-12ef-46b2-9724-0aeca7b62827","tagId":"[tag_id]", "transactionId":"00000000-0000-0000-0000-000000000000", "stoptime":"YYYY-MM-DDTHH:MM:SSZ"}'
    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/uuid/start', 
    headers=headers, data=data)
    print(response) #debugging
    

#Notify Start (request sent by charger)
def notifyStart(token):
    print("notifyStart")
    #serverNotify = requests.get(APIServer + '/ServicesApi/rest/charger/uuid/start')
    #if (serverNotify.status_code == 200):
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    data = '{"accepted" : true,"errorCode" : "NO_ERROR"}'

    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/uuid/start', 
    headers=headers, data=data)
#else: 
    #print(serverNotify)
    #print(serverNotify.text)
    print(response)
    print(response.text)

#Stop Charger
def stopCharger(token):
    print("stopCharger")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    data = '{"evseId" : "d4ceb292-12ef-46b2-9724-0aeca7b62827", "transactionId" : "00000000-0000-0000-0000-000000000000"}'

    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/uuid/stop', 
    headers=headers, data=data)
    print(response)

#Notify Stop (request sent by charger)
def notifyStop(token):
    print("notifyStop")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    data = '{"accepted" : true,"errorCode" : "NO_ERROR"}'

    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/uuid/stop', 
    headers=headers, data=data)
    print(response)
    print(response.text)

#Change Active Current (amps)
def changeActiveCurrent(token):
    print("changeActiveCurrent")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    data = '{"current": "[current]", "chargeboxidentity": "000005354-1","connectorid": "1"}'

    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/changeactivecurrent', 
    headers=headers, data=data)
    print(response)
    print(response.text)
#Consumed Energy (KWh) / duration
def consumedEnergy(token):
    print("consumedEnergy")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    data = '{"tagId" : "[tag_id]", "intervalStart" : "YYYY-MM-DD"," intervalEnd" : "YYYY-MM-DD"}'

    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/tag/getSessionsByTag', 
    headers=headers, data=data)
    print(response)
    print(response.text)

#Request Site Info
def requestSiteInfo(token):
    print("requestSiteInfo")
    headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json',
    }

    data = '{"siteid" : "6d411116-91cc-4a61-9b83-b83380a04e69"}'
    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/siteinfo', 
    headers=headers, data=data)
    print(response)

#Get Connector Status

#Set RFID tagID

#Request RFID tagID info
