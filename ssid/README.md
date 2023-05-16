# Task: auto ssid info upate & request

## Intro:
- python3.10, using requests, qrcode, boto3 for the task
- include 2 functions:
  - (api) get ssid infor and generate qrcode + upload to s3
  - (api) post (update) ssid (psk) ..: 
- automation:
  - scheduled 2 above functions to change psk daily and periodically (ie. 10 min) get and generate the qrcode.
 
## deploy on aws lambda how to:
1. on dev machine
- package/ dependency preparation:
  -  mkdir -p temp/python
  -  cd temp/
  -  python3.10 -m pip install requests -t python
  -  zip -r lambda_layer_requests.zip python
  
2. on aws
- create layer with above zip file
- create 'lambda_function.py'
  - get/post API
  - generated qr code
  - upload to s3

3. on s3 (for static website)
- create index.html for qr-image ref. 
- note: no-cache metadata,  .. cognitor browser ..

