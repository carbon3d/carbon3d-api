#!/usr/bin/env python3

import sys
import json
import time
import argparse
import logging

from http.client import HTTPConnection
import jwt

HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
REQUESTS_LOG = logging.getLogger("requests.packages.urllib3")
REQUESTS_LOG.setLevel(logging.DEBUG)
REQUESTS_LOG.propagate = True


def create_api_token(key_file: str, exp_minutes: int) -> str:
    """
    Creates api token to authorize api usage
    Args:
        key_file: JSON file that contains client_id and client_secret
        exp_minutes: Number of minutes before api token expires
    Returns:
        str: jwt token
    """
    with open(key_file, 'r') as secrets_file:
        secret_content = secrets_file.read()
        secret_json = json.loads(secret_content)
    client_id = secret_json['client_id']
    client_secret = secret_json['client_secret']

    # Generate jwt token
    jwt_contents = {
        'iss': client_id,
        'exp': int(time.time() + exp_minutes * 60)
    }

    # Sign & encode token with client secret
    encoded_jwt = jwt.encode(
        jwt_contents,
        client_secret,
        algorithm='RS256'
    )

    # Versions of pyjwt before v2.0.0 return bytes
    if isinstance(encoded_jwt, bytes):
        encoded_jwt = encoded_jwt.decode("utf-8")

    return encoded_jwt


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='secrets.json file with client_id and client_secret')
    parser.add_argument('--exp_minutes', '-e', help='token expiration (minutes)', type=int, default=60)

    # Create JWT Token from API key
    args = parser.parse_args()
    try:
        print(create_api_token(args.file, args.exp_minutes))
    except Exception as e:
        print("Exception when creating token:\n%s\n" % e, file=sys.stderr)
        print(args)
