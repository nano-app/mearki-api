import json
import boto3
import requests
import qrcode
import os



# funct. upload file to s3
def upload_file_to_s3(file_path, bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    file_name = file_path.split('/')[-1]  # Extracting just the file name from the file path
    
    
    try:
        bucket.upload_file(file_path, file_name)
        print(f"File '{file_name}' uploaded successfully to S3 bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Error uploading file '{file_name}' to S3 bucket '{bucket_name}': {str(e)}")

# funct. generate qr from input string and upload image to s3
def gen_qr_and_upload_s3(source_string, bucket_name):
    
    img = qrcode.make(source_string)
    img.save('/tmp/outputqr.png')    
    file_path = '/tmp/outputqr.png'
    upload_file_to_s3(file_path, bucket_name)
    print('gen qrcode and upload s3 successfully')

# MAIN function: request ssid info, parsing json result, call qr generating and upload to s3
def lambda_handler(event, context):
    # TODO implement
    bucket_name = os.environ['BUCKET_NAME']
    my_api_key = os.environ['API_KEY']
    ipsk_url = os.environ['API_IPSK_URL']
    
    #1. Get ssid info
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": my_api_key
        }
    payload = None
    
    try:
        response = requests.request('GET', ipsk_url, headers=headers, data = payload)
        print(response)
        
        # 2. gen qr and upload to s3
        # extract ssid info from json result
        json_data = json.loads(response.text.encode('utf8'))
        print(json_data)
        
        # should be requestd, another request URL
        ssid_name = "TestIPSK"
        ssid_encmode = "WPA"
        
        ssid_ipsk = json_data[0]['passphrase']
        
        
            # wifi string format 
            # WIFI:S:<ssid_name>;T:WPA;P:<password>;H:false;;
        ssid_string = 'WIFI:S:' + ssid_name + ';T:' + ssid_encmode+';P:' + ssid_ipsk + ';H:false;;'
        
        gen_qr_and_upload_s3(ssid_string, bucket_name)
        
        return {
            'statusCode': 200,
            'body': json.dumps('get ssid result: ' + ssid_string)
        }
        
    except Exception as e:
        print(f"Error in main function': {str(e)}")
