#!/usr/bin/env python3

import time
import carbon
from carbon.rest import ApiException
from pprint import pprint
import os

import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--model_id', '-m', help='API URL prefix')
my_parser.add_argument('--part_number', '-p')
my_parser.add_argument('--limit', '-l', default=100, type=int)
my_parser.add_argument('--offset', '-o', default=0, type=int)
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

try:
    # Upload a model
    api_response = api.get_models(
        model_id=args.model_id,
        part_number=args.part_number,
        limit=args.limit,
        offset=args.offset
    )
    pprint(api_response)
except ApiException as e:
    print('Exception when calling ModelsApi->get_models: %s\n' % e)
