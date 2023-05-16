Task: auto ssid info upate & request

# deploy on aws lambda how to:
1. on dev machine
- pip install requests, qrcode .. -t some/folder
- zip -r some/folder

2. on aws
- create layer with created zip file
- create 'lambda_function.py'
  - get/post API
  - generated qr code
  - upload to s3

3. s3 (for static website)
- create index.html for qr-image ref. 
- note: no cache setting .. cognitor browser ..

