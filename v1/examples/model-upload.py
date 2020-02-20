#!/usr/bin/env python3

import time
import carbon
from carbon.rest import ApiException
from pprint import pprint

import argparse

# To debug requests API requests:
import requests
import logging
from http.client import HTTPConnection
HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


my_parser = argparse.ArgumentParser()
my_parser.add_argument('file', help='model file')
my_parser.add_argument('--model_id', '-m', required=True)
my_parser.add_argument('--part_number', '-p', required=True)
my_parser.add_argument('--access_token', '-t',
                       help='JWT Access Token', required=True)
my_parser.add_argument('--api', '-a', help='API URL prefix',
                       default='https://api-sandbox.carbon3d.com/v1')
args = my_parser.parse_args()

configuration = carbon.Configuration(host=args.api)

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = args.access_token

# Create an instance of the API class
api = carbon.ModelsApi(carbon.ApiClient(configuration))

pprint(args)
try:
    # Upload a model
    api_response = api.add_model(
        args.model_id, args.part_number, file=args.file)
    pprint(api_response)
except ApiException as e:
    print('Exception when calling ModelsApi->add_model: %s\n' % e)
