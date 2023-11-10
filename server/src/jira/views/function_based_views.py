# import json, requests
# from requests.auth import HTTPBasicAuth

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.request import Request
# from rest_framework import status

# token = 'ATATT3xFfGF0i9GV4lt-5sc5ew5jQm-KFYBtSPCHVtbwgulYm_uSvsntKN1tVnGqZrvcqfKFLnUXtMuS9yaBMR4cP_24hArPBacCAr_IU6JN2mn0I-15Lf7qL1OXid-HJoRP83S7NnvthF8OZLUpH9qai0zygvckXyQgyqZOiuAuMQ9Tg7eY9Xk=862FC402'

# @api_view(['POST'])
# def getResource(request: Request) -> Response:

#     request_url = request.data.get('url')
#     request_headers = request.data.get('header')
#     request_email = request.data.get('email')

#     if (
#         request_url is None or
#         request_headers is None or
#         request_email is None
#     ):
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     authentication = HTTPBasicAuth(request_email, token)
#     jira_response = requests.request(
#         method="GET", 
#         url=request_url, 
#         headers=request_headers,
#         auth=authentication
#     )

#     return Response(jira_response.text)

import os
import json
import json, requests
from requests.auth import HTTPBasicAuth
from pathlib import Path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

# Getting the absolute path of the current script
current_script_path = Path(__file__).resolve()

# Constructing the path to keys-dev.json based on the current script's directory
project_root = current_script_path.parent.parent.parent.parent
keys_dev_path = project_root / 'config' / 'keys-dev.json'

# Reading the keys-dev.json file
with open(keys_dev_path, 'r') as json_file:
    keys_data = json.load(json_file)

# Extracting the Jira token from the keys_data
jira_token = keys_data.get('jira_tokens', [{}])[0].get('token', '')
print("JIRA TOKEN: ", jira_token)

@api_view(['POST'])
def getResource(request: Request) -> Response:
    request_url = request.data.get('url')
    request_headers = request.data.get('header')
    request_email = request.data.get('email')

    if request_url is None or request_headers is None or request_email is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # Extract the Jira site from the provided URL
    #request_url = "https://multi-llm.atlassian.net/rest/api/3/issue/picker"
    jira_site = '/'.join(request_url.split('/')[:3])

    # Read the Jira token from keys-dev.json based on the Jira site
    for token_info in keys_data.get('jira_tokens', []):
        if token_info.get('site') == jira_site:
            jira_token = token_info.get('token', '')
            break

    if not jira_token:
        return Response({'error': 'Jira token not found for the provided site'}, status=status.HTTP_400_BAD_REQUEST)

    authentication = HTTPBasicAuth(request_email, jira_token)
    jira_response = requests.request(
        method="GET", 
        url=request_url, 
        headers=request_headers,
        auth=authentication
    )

    return Response(jira_response.text)