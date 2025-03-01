import boto3
import json
import requests
import webbrowser

# Initialize STS client with your AWS credentials
sts_client = boto3.client('sts')

# Get temporary credentials
session = sts_client.get_session_token()
credentials = session['Credentials']

# Generate federation token request
federation_url = "https://signin.aws.amazon.com/federation"
session_json = json.dumps({
    "sessionId": credentials["AccessKeyId"],
    "sessionKey": credentials["SecretAccessKey"],
    "sessionToken": credentials["SessionToken"]
})

# Get the Sign-in Token
token_response = requests.get(f"{federation_url}?Action=getSigninToken&Session={session_json}")
signin_token = json.loads(token_response.text)["SigninToken"]

# Construct the AWS console login URL
console_url = f"{federation_url}?Action=login&Issuer=Example&Destination=https://console.aws.amazon.com/&SigninToken={signin_token}"

# Open the URL in the default web browser
print(f"Login URL: {console_url}")
webbrowser.open(console_url)
