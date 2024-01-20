import requests
import base64
import hashlib
import pyotp
import json
import sys

#similar source code written in javascript at stack overflow
#https://stackoverflow.com/questions/62358166/how-to-solve-the-problem-of-access-denied-invalid-token-wrong-code

"""

I am testing a multi line comment and seems to be working fine. Cool!

"""

# Construct the JSON string for the link to mission one
ReqJSON = {
    "github_url": "https://gist.github.com/dsamist/3d4d1b458482a816c9fd6872fe9ab57d",
    "contact_email": "s.eneojo.emmanuel@gmail.com",
    "solution_language": "python"
}

# Convert the dictionary to a JSON string
stringData = json.dumps(ReqJSON)

# API endpoint to send the POST request
URL = 'https://api.challenge.hennge.com/challenges/003'

# The secret key for TOTP generation
sharedSecret = 's.eneojo.emmanuel@gmail.comHENNGECHALLENGE003'

# Convert the shared secret to Base32 encoding for TOTP
base32_shared_secret = base64.b32encode(sharedSecret.encode()).decode()

# Initialize TOTP instance with the Base32-encoded secret
totp = pyotp.TOTP(base32_shared_secret, digits=10, digest=hashlib.sha512)

# Generate the current TOTP
MyTOTP = totp.now()

# Create the string for Authorization header in format: contact_email:MyTOTP
authStringUTF = ReqJSON['contact_email'] + ':' + MyTOTP

# Encode the string to bytes using UTF-8 encoding (This is necessary because when sending data over networks or 
#using cryptographic functions, they often expect binary data (bytes) rather than string data.)
bytes = authStringUTF.encode('utf-8')

# Encode the bytes to Base64 string
encoded = base64.b64encode(bytes).decode('utf-8')

# Create headers for the POST request with Content-Type and Authorization
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + encoded,
}

# Send a POST request with the JSON data and headers
response = requests.post(URL, data=stringData, headers=headers)

# Print the response from the server
print(response.json())
