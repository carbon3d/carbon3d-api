#!/usr/bin/env python3

import argparse
import logging
import time
from datetime import datetime, timedelta, timezone
from http.client import HTTPConnection
from pprint import pprint

import carbon3d
# To debug requests API requests:
import requests
from carbon3d.rest import ApiException
from dateutil import tz

HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


my_parser = argparse.ArgumentParser()
my_parser.add_argument(
    'model_id', help='model identifier', action='store', nargs='*')
my_parser.add_argument('--part_number', '-p', required=True)
my_parser.add_argument('--order_id', '-o', required=True)
my_parser.add_argument('--access_token', '-t',
                       help='JWT Access Token', required=True)
my_parser.add_argument('--api', '-a', help='API URL prefix',
                       default='https://api-sandbox.carbon3d.com/v1')
args = my_parser.parse_args()

configuration = carbon3d.Configuration(host=args.api)

# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = args.access_token

# Create an instance of the API class
api_instance = carbon3d.OrdersApi(carbon3d.ApiClient(configuration))

due_date = datetime.today() + timedelta(days=10)
parts = [
    ({"part_number": args.part_number, "model_id": id}) for id in args.model_id
]


def format_date(date):
    return date.astimezone(tz.gettz('UTC')).replace(microsecond=0).isoformat()


order = carbon.Order(
    order_id=args.order_id,
    parts=parts,
    due_date=format_date(due_date)
)
pprint(order)
try:
    # Create an Order
    api_response = api_instance.create_order(order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->create_order: %s\n" % e)
