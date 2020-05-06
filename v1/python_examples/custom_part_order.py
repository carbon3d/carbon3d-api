#!/usr/bin/env python3

import argparse
import datetime
import json
import logging
import os
import re
import time
from typing import List

import dateutil
import jwt
import carbon3d as carbon



#Set up logger
LOG = logging.getLogger('customer_part_order')
FILE_HANDLER = logging.FileHandler('customer_part_order.log')
CONSOLE_HANDLER = logging.StreamHandler()
FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(filename)s:%(lineno)d %(message)s')
FILE_HANDLER.setFormatter(FORMATTER)
CONSOLE_HANDLER.setFormatter(FORMATTER)
LOG.addHandler(FILE_HANDLER)
LOG.addHandler(CONSOLE_HANDLER)
LOG.setLevel(logging.INFO)

def create_api_token(key_file: str, exp_minutes: int) -> str:
    """
    Creates api token to authorize api usage
    Args:
        key_file: JSON file that contains client_id and client_secret
        exp_minutes: Number of minutes before api token expires
    Returns:
        str: jwt token
    """
    LOG.info('create_api_token: key_file={} exp_minutes={}'.format(key_file, exp_minutes))
    with open(key_file, 'r') as secrets_file:
        secret_content = secrets_file.read()
        secret_json = json.loads(secret_content)
    client_id = secret_json['client_id']
    client_secret = secret_json['client_secret']

    # Generate jwt token
    jwt_contents = {
        'iss': client_id,
        'exp': int(time.time() + exp_minutes*60*60)
    }

    # Sign & encode token with client secret
    encoded_jwt = jwt.encode(
        jwt_contents,
        client_secret,
        algorithm='RS256'
    )
    return encoded_jwt.decode('utf-8')

def upload_model(models_api: carbon.ModelsApi,
                 application_id: int,
                 file_path: str) -> carbon.models.model.Model:
    """
    Uploads a model
    Args:
        models_api: Authenticated Models Api
        application_id: Application id
        file_path: File path to model
    Returns:
        carbon.models.model.Model
    """
    LOG.info('upload_model: file_path={}'.format(file_path))
    filename = os.path.basename(file_path)
    with open(file_path, 'rb') as mesh_file:
        api_response = models_api.upload_model(
            filename,
            application_id=application_id,
            body=mesh_file.read()
        )
    LOG.info('upload_model: api_response={}'.format(str(api_response).replace('\n', ' ')))
    return api_response

def create_part(parts_api: carbon.PartsApi,
                part_catalog_num: str,
                model_uuid: str,
                application_id: int) -> carbon.models.part.Part:
    """
    Creates a part
    Args:
        parts_api: Authenticated Parts Api
        part_catalog_num: Part catalog number
        model_uuid: Uploaded Model uuid
        application_id: Application id
    Returns:
        carbon.models.part.Part
    """
    LOG.info('create_part: part_catalog_num={} model_uuid={}'.format(part_catalog_num, model_uuid))
    part_request = carbon.PartRequest(part_number=part_catalog_num,
                                      model_uuid=model_uuid,
                                      application_id=application_id)
    api_response = parts_api.create_part(part_request=part_request)
    LOG.info('create_part: api_response={}'.format(str(api_response).replace('\n', ' ')))
    return api_response

def create_order(orders_api: carbon.OrdersApi,
                 order_number: str,
                 parts: List[carbon.models.part.Part],
                 due_date: datetime.datetime) -> carbon.models.order.Order:
    """
    Creates an order
    Args:
        orders_api: Authenticated Orders Api
        order_number: Order number
        parts: List of parts
        due_date: Due date of order
    Returns:
        carbon.models.order.Order
    """
    LOG.info('create_order: parts={}'.format(str(parts).replace('\n', ' ')))
    order_request_parts = [carbon.OrderRequestParts(part.uuid) for part in parts]
    order_request = carbon.OrderRequest(order_number=order_number,
                                        parts=order_request_parts,
                                        due_date=due_date)
    api_response = orders_api.create_order(order_request=order_request)
    LOG.info('create_order: api_response={}'.format(re.sub(' +', ' ', (re.sub('\t|\n', ' ', str(api_response))))))
    return api_response

def main():

    parser = argparse.ArgumentParser(description='Script to upload models, create parts, and create an order',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     add_help=True)
    parser.add_argument('--application_id',
                        '-a',
                        help='Application scope for part number',
                        type=int,
                        default=0)
    parser.add_argument('--host',
                        help='Carbon API host',
                        default='https://api.carbon3d.com/v1')
    parser.add_argument('--part_catalog_num',
                        '-p',
                        help='Part catalog number i.e. ALIGNER-001',
                        required=True)
    parser.add_argument('--order_number',
                        '-o',
                        help='Order number',
                        required=True)
    parser.add_argument('--due_date',
                        '-d',
                        type=float,
                        help='Number of days from today for order due date to be set',
                        required=True)
    parser.add_argument('--secret',
                        '-s',
                        help='JSON file with client_id and client_secret',
                        required=True)
    parser.add_argument('files',
                        nargs='+',
                        help='Model file paths (.stl)')
    args = parser.parse_args()
    LOG.info('main: Start. args={}'.format(args))


    # Assemble stls list
    if args.files:
        stls = args.files
    else:
        raise Exception("No model files were given")

    LOG.info('main: stls={}'.format(stls))

    config = carbon.Configuration(host=args.host)

    # Configure Bearer authorization (JWT): bearerAuth
    config.access_token = create_api_token(args.secret, 5)

    # Prepare APIs
    models_api = carbon.ModelsApi(carbon.ApiClient(config))
    parts_api = carbon.PartsApi(carbon.ApiClient(config))
    orders_api = carbon.OrdersApi(carbon.ApiClient(config))

    # Upload models
    models = []
    for file_path in stls:
        models.append(upload_model(models_api, args.application_id, file_path))
    LOG.info('main: models={}'.format(str(models).replace('\n', ' ')))

    # Create parts
    parts = []
    for model in models:
        parts.append(create_part(parts_api, args.part_catalog_num, model.uuid, args.application_id))
    LOG.info('main: parts={}'.format(str(parts).replace('\n', ' ')))

    # Create order
    due_date = datetime.datetime.today() + datetime.timedelta(days=args.due_date)
    formatted_due_date = due_date.astimezone(dateutil.tz.gettz('UTC')).replace(microsecond=0).isoformat()
    create_order(orders_api, args.order_number, parts, formatted_due_date)

    LOG.info('main: End')

if __name__ == "__main__":
    main()
