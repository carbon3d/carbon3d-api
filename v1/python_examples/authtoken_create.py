#!/usr/bin/env python3

import sys
import json
import time
import argparse
import logging

from http.client import HTTPConnection
import jwt

HTTPConnection.debuglevel = 1  # type: ignore
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
REQUESTS_LOG = logging.getLogger("requests.packages.urllib3")
REQUESTS_LOG.setLevel(logging.DEBUG)
REQUESTS_LOG.propagate = True


MY_PARSER = argparse.ArgumentParser()
MY_PARSER.add_argument('file', help='secrets.json file with client_id and client_secret')
MY_PARSER.add_argument('--exp_minutes', '-e', help='token expiration (minutes)', type=int, default=60)

ARGS = MY_PARSER.parse_args()

def create_api_token(key_file, exp_minutes):
    try:
        with open(key_file, 'r') as secrets_file:
            secret_content = secrets_file.read()
            secret_json = json.loads(secret_content)
        client_id = secret_json['client_id']
        client_secret = secret_json['client_secret']
        # generate jwt token
        jwt_contents = {
            'iss': client_id,
            'exp': int(time.time() + exp_minutes*60)
        }
        # sign & encode token with client secret
        encoded_jwt = jwt.encode(
            jwt_contents,
            client_secret,
            algorithm='RS256'
        )
        # output token
        print(encoded_jwt.decode('utf-8'))
    except Exception as e:
        print("Exception when creating token:\n%s\n" % e, file=sys.stderr)
        print(ARGS)

if __name__ == "__main__":
    # Create JWT Token from API key
    create_api_token(ARGS.file, ARGS.exp_minutes)
