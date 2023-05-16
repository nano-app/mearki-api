# Change the PSK of pre-defined SSID via API

import json
import requests
import os

def verify_ssid_name():
    
    #1. Get ssid info
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": os.environ['API_KEY']
        }
    payload = None
    
    try:
        response = requests.request('GET', os.environ['API_SSID_URL'], headers=headers, data = payload)
        json_data = json.loads(response.text.encode('utf8'))
        ssid_name = json_data['name']
        
        if ssid_name == os.environ['TARGET_SSID']:
            #print(ssid_name)
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Error in main function': {str(e)}")
        return False
        

def lambda_handler(event, context):
    # verify the right network and ssid befor updating !!! (ssid name = target name?)
    if verify_ssid_name() == True:
        
        os.environ['API_SSID_URL'] 
        my_api_key = os.environ['API_KEY']
        ssid_url = os.environ['API_SSID_URL']
        
        # random or pre-defined list here
        new_psk = '"updated165c"'
        
    
        try:
            # header and load
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": my_api_key
            }
            
            payload = '{"psk": ' + new_psk + '}'
    
            response = requests.request('PUT', ssid_url, headers=headers, data = payload)
    
        except Exception as e:
            print(f"Error found {str(e)}")
            
    else:
        print("ssid not verified, cancel update")
        
    return {
        'statusCode': 200,
        'body': json.dumps('result: ')
    }

