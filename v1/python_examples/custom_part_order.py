#!/usr/bin/env python3

import argparse
from datetime import datetime, timezone, timedelta
import json
import logging
import os
import re
import time
from typing import List

import jwt
import carbon3d as carbon


# Set up logger
LOG = logging.getLogger('customer_part_part_order')
FILE_HANDLER = logging.FileHandler('customer_part_part_order.log')
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

def upload_model(models_api: carbon.ModelsApi,
                 application_uuid: str,
                 file_path: str) -> carbon.models.model.Model:
    """
    Uploads a model
    Args:
        models_api: Authenticated Models Api
        application_uuid: Application uuid
        file_path: File path to model
    Returns:
        carbon.models.model.Model
    """
    LOG.info('upload_model: file_path={}'.format(file_path))
    filename = os.path.basename(file_path)
    with open(file_path, 'rb') as mesh_file:
        api_response = models_api.upload_model(
            filename,
            application_uuid=application_uuid,
            body=mesh_file.read()
        )
    LOG.info('upload_model: api_response={}'.format(str(api_response).replace('\n', ' ')))
    return api_response

def create_part(parts_api: carbon.PartsApi,
                part_catalog_num: str,
                model_uuid: str,
                application_uuid: str) -> carbon.models.part.Part:
    """
    Creates a part
    Args:
        parts_api: Authenticated Parts Api
        part_catalog_num: Part catalog number
        model_uuid: Uploaded Model uuid
        application_uuid: Application uuid
    Returns:
        carbon.models.part.Part
    """
    LOG.info('create_part: part_catalog_num={} model_uuid={}'.format(part_catalog_num, model_uuid))
    part_request = carbon.PartRequest(part_number=part_catalog_num,
                                      model_uuid=model_uuid,
                                      application_uuid=application_uuid)
    api_response = parts_api.create_part(part_request=part_request)
    LOG.info('create_part: api_response={}'.format(str(api_response).replace('\n', ' ')))
    return api_response

def create_part_order(part_orders_api: carbon.PartOrdersApi,
                      part_order_number: str,
                      parts: List[carbon.models.part.Part],
                      due_date: datetime,
                      flush: bool,
                      build_sop_uuid: str) -> carbon.models.part_order.PartOrder:
    """
    Creates an part_order
    Args:
        part_orders_api: Authenticated PartOrders Api
        part_order_number: PartOrder number
        parts: List of parts
        due_date: Due date of part_order
        flush: Immediately send parts to be packed into a build
        build_sop_uuid: Build SOP UUID
    Returns:
        carbon.models.part_order.PartOrder
    """
    LOG.info('create_part_order: parts={}'.format(str(parts).replace('\n', ' ')))
    part_order_request_parts = [{'uuid': part.uuid} for part in parts]
    part_order_request = carbon.PartOrderRequest(part_order_number=part_order_number,
                                                 parts=part_order_request_parts,
                                                 due_date=due_date,
                                                 flush=flush,
                                                 build_sop_uuid=build_sop_uuid)
    api_response = part_orders_api.create_part_order(part_order_request=part_order_request)
    LOG.info('create_part_order: api_response={}'.format(re.sub(' +', ' ', (re.sub('\t|\n', ' ', str(api_response))))))
    return api_response

def main():

    parser = argparse.ArgumentParser(description='Script to upload models, create parts, and create an part_order',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     add_help=True)
    parser.add_argument('--application_uuid',
                        '-a',
                        help='Application scope for part number',
                        type=str,
                        )
    parser.add_argument('--host',
                        help='Carbon API host',
                        default='https://api.carbon3d.com/v1')
    parser.add_argument('--part_catalog_num',
                        '-p',
                        help='Part catalog number i.e. ALIGNER-001',
                        required=True)
    parser.add_argument('--part_order_number',
                        '-o',
                        help='Part order number',
                        required=True)
    parser.add_argument('--due_date',
                        '-d',
                        type=float,
                        help='Number of days from today for part_order due date to be set',
                        required=True)
    parser.add_argument('--flush',
                        '-f',
                        help='Flush part order',
                        action='store_true',
                        default=False)
    parser.add_argument('--build_sop_uuid',
                        '-b',
                        help='Build sop uuid',
                        )
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
    part_orders_api = carbon.PartOrdersApi(carbon.ApiClient(config))

    # Upload models
    models = []
    for file_path in stls:
        models.append(upload_model(models_api, args.application_uuid, file_path))
    LOG.info('main: models={}'.format(str(models).replace('\n', ' ')))

    # Create parts
    parts = []
    for model in models:
        parts.append(create_part(parts_api, args.part_catalog_num, model.uuid, args.application_uuid))
    LOG.info('main: parts={}'.format(str(parts).replace('\n', ' ')))

    # Create part_order
    due_date = datetime.now(timezone.utc) + timedelta(days=args.due_date)
    formatted_due_date = due_date.replace(microsecond=0).isoformat().replace("+00:00", "Z")
    create_part_order(part_orders_api, args.part_order_number, parts, formatted_due_date,
                      args.flush, args.build_sop_uuid)

    LOG.info('main: End')


if __name__ == "__main__":
    main()
