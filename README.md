# AWSKey2Console
A simple Python script that can log you into the aws console just with your access key and secret key. Get GUI from CLI ;)

###Steps to run
1. Install the AWS CLI if not already installed. (Verify it by "aws --version")
2. Configure the aws credential to your default profile
3. Run "aws configure" and enter the secret key and access key leave the other fields intact
4. Install required Python packages using "pip install boto3 requests"
5. run this Python file on your machine "python aws_console_login.py"
6. Take the URL and open in browser to get the Console

NOTE: this console URL will be valid for a limited time only

