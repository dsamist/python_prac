import requests
import json
import hmac
import hashlib
import base64
import time
import struct
import sys

# Construct the JSON string
data = {
    "github_url": "https://gist.github.com/dsamist/3d4d1b458482a816c9fd6872fe9ab57d",
    "contact_email": "s.eneojo.emmanuel@gmail.com",
    "solution_language": "python"
}

# Generate the TOTP password

def generate_totp():

    shared_secret = "s.eneojo.emmanuel@gmail.comHENNGECHALLENGE003"
    time_step = 30  # seconds
    #T0 = 0

    # # Get the current time in seconds since the Unix epoch, divided by the time step
    T = int(time.time()) // time_step


    # Generate the HMAC-SHA-512 hash
    message = bytes(str(T), 'utf-8')
    digest = hmac.new(bytes(shared_secret, 'utf-8'), message, hashlib.sha512).digest()

    # Extract the 4-byte dynamic binary code
    offset = digest[-1] & 0x0f
    binary = int.from_bytes(digest[offset:offset+4], byteorder='big') & 0x7fffffff

    # Format the code as a 10-digit string
    #totp = str(binary)[-10:].zfill(10)
    totp = str(binary % 10**10).zfill(10)

    return totp

totp = generate_totp()
print("TOTP password:", totp)

# sys.exit()
encode_parameters = base64.b64encode(f"s.eneojo.emmanuel@gmail.com:{totp}".encode())
decoded_string = encode_parameters.decode('utf-8')
print(decoded_string)


# Make the POST request
# Send an HTTP POST request to the provided URL with headers including Authorization using the calculated TOTP
response = requests.post(
    "https://api.challenge.hennge.com/challenges/003",
    headers={
        'Content-Type': 'application/json',
        #"Authorization": ("Basic " + f"{decoded_string}")
        'Authorization': f'Basic {decoded_string}',
        'Accept': '*/*',
        'Content-Length': '133'
    },
    # data=json.dumps(data)
    json=data
)

print(f'Basic {decoded_string}')

# Check the response
# Check the response status code for success or failure
if response.status_code == 200:
    print("Success!")
else:
    print("Failed:", response.status_code, response.text)
