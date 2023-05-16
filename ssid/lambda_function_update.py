# Update the SSID psk
# Change the file name to able to run on lambda (lambda_function.py)
# CAUTION !!!! --> verifiy URL, network, ssid ID before run .. need to code this 
# TODO: implement network, ssid verification before update.


import json
import requests
import os

def lambda_handler(event, context):
    # TODO implement
    my_api_key = os.environ['API_KEY']
    ssid_url = os.environ['API_SSID_URL']
    
    try:
        # header and load
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": my_api_key
        }
        payload = '''{
            "psk": "autokeyupdated165"
        }'''
        
        response = requests.request('PUT', ssid_url, headers=headers, data = payload)

    except Exception as e:
        print(f"Error found {str(e)}")
        
    return {
        'statusCode': 200,
        'body': json.dumps('result: ' + str(response.text.encode('utf8')))
    }
