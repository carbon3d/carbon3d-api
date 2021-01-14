#!/usr/bin/env python3

# Class to export cvs of printed parts via Carbon3D API, optionally filtered and/or sorted
# Can be imported and called as part of a more complete API interface by passing existing api client for config,
# Or run as a standalone utility with an optional output path (defaults to stdout):
# ./printed_parts_csv_exporter.py optional_path/to/output.csv -s path/to/secret.json \
#   --max_records 550 --filter_options '{"print_id":[1234]}' --sort_options "updated_at,desc" "uuid,asc"
import argparse
import json
import sys
from distutils.version import LooseVersion as version
from math import ceil
from time import time, sleep
from typing import Union
import numpy as np
import pandas as pd
import jwt
from carbon3d import (ApiClient, Configuration, PrintsApi, PrintedPartsApi, __version__ as client_version)

# API responses are limited to 100 responses per page - this value should not be changed
MAX_LIMIT = 100
# API allows up to 100 values per filter per request
FILTER_LIMIT = 100
# API server rate limits incoming requests - add a delay between requests to avoid 429s
REQ_DELAY_S = 1 /5

def get_next_limit(page: int,
                   max_records: int) -> int:
    """Compute limit for next request based on user specified max records and max per request limit"""
    if (max_records - ((page) * MAX_LIMIT)) > MAX_LIMIT:
        return MAX_LIMIT
    return max_records - ((page) * MAX_LIMIT)

class Carbon3dCsvExporter():
    """Export CSV of printed_parts joined with prints"""
    def __init__(self,
                 api_client: ApiClient) -> None:
        if client_version < version('0.2.2'):
            sys.exit('Requires carbon3d-client version of at least 0.2.2, ({v} found)'.format(v=client_version) +
                     '\nUpdate with: pip install --upgrade carbon3d-client')

        self.printed_parts_api = PrintedPartsApi(api_client)
        self.prints_api = PrintsApi(api_client)

    def export_printed_parts(self,
                             export_path: Union[str, None],
                             filter_options: dict = None,
                             sort_options: list = None,
                             max_records: int = 1000) -> None:
        """
        Gets printed parts and associated print records, then outputs to csv file
        Args:
            export_path: path to output csv results
            filter_options: optional parameters to filter printed_parts by
            sort_options: optional parameters to sort printed_parts response by
            max_records: maximumum number of printed parts to request for output to csv
        """
        printed_parts = self.get_printed_parts(filter_options, sort_options, max_records)
        prints = self.get_prints(printed_parts.print_id.unique().tolist())
        joined_records = pd.merge(printed_parts, prints, on='print_id', how='left', suffixes=[None, " (print)"])

        if export_path:
            joined_records.to_csv(export_path)
        else:
            joined_records.to_csv(sys.stdout)

    def get_printed_parts(self,
                          filter_options: dict = None,
                          sort_options: list = None,
                          max_records: int = None) -> pd.DataFrame:
        """
        Get printed_part records for filter options
        Args:
            filter_options: optional parameters to filter printed_parts by
            sort_options: optional parameters to sort printed_parts response by
            max_records: maximumum number of printed parts to request for output to csv
        """
        extra_args = {}  # type: dict
        if filter_options:
            extra_args.update(filter_options)

        printed_parts = pd.DataFrame()
        for page in range(ceil(max_records / 100)):
            limit = get_next_limit(page, max_records)
            response = self.printed_parts_api.get_printed_parts(
                limit=limit, sort=sort_options, **extra_args)
            sleep(REQ_DELAY_S)
            if response.next_cursor:
                extra_args.update({'cursor': response.next_cursor})
            else:
                extra_args.pop('cursor', None)
            for printed_part_record in response.parts:
                printed_parts = printed_parts.append(printed_part_record.to_dict(), ignore_index=True)
            if len(printed_parts) >= response.total_count:
                break

        return printed_parts

    def get_prints(self,
                   print_ids: list) -> pd.DataFrame:
        """
        Get print records for print_ids
        Args:
            print_ids: list of print_ids to get print response info for
        """
        # Chunk the print_id list to stay within filter value limit
        n_chunks = ceil(len(print_ids) / FILTER_LIMIT)
        chunked_print_ids = np.array_split(print_ids, n_chunks)

        prints = pd.DataFrame()
        for print_id_chunk in chunked_print_ids:
            response = self.prints_api.get_prints(limit=MAX_LIMIT, print_id=print_id_chunk.tolist())
            sleep(REQ_DELAY_S)
            for print_record in response.prints:
                prints = prints.append(print_record.to_dict(), ignore_index=True)
        return prints

def main():
    """Export csv of printed_part records joined with print_record when invoked from command line"""
    parser = argparse.ArgumentParser(
        description='Get and export PrintedParts data to CSV',
        epilog='see https://api.carbon3d.com/v1/api-docs/#/Printed%20Parts for permitted filter and sort options')
    parser.add_argument('export_path',
                        type=str,
                        nargs='?',
                        help='Output csv filepath')
    parser.add_argument('--secret',
                        '-s',
                        help='JSON file with client_id and client_secret',
                        required=True)
    parser.add_argument('--token_exp_minutes',
                        type=int,
                        default=15,
                        help='Length of generated token validity')
    parser.add_argument('--host',
                        help='Carbon API host',
                        default='https://api.carbon3d.com/v1')
    parser.add_argument('--filter_options',
                        '-f',
                        type=str,
                        help='JSON formatted filter(s), e.g.: \'{"print_id":[1234]}\'')
    parser.add_argument('--sort_options',
                        '-o',
                        type=str,
                        nargs='+',
                        help='List of sort option(s) e.g: "updated_at,desc" "uuid,asc"')
    parser.add_argument('--max_records',
                        '-m',
                        type=int,
                        default=1000,
                        help='Maximum number of results to return')

    args = parser.parse_args()
    with open(args.secret, 'r') as secret_file:
        secret_content = secret_file.read()
        secret_json = json.loads(secret_content)
    client_id = secret_json['client_id']
    client_secret = secret_json['client_secret']

    jwt_contents = {
        'iss': client_id,
        'exp': int(time() + args.token_exp_minutes * 60)
    }
    jwt_token = jwt.encode(jwt_contents, client_secret, algorithm='RS256').decode('utf-8')

    if args.filter_options:
        filter_options = json.loads(args.filter_options)
    else:
        filter_options = None

    config = Configuration(args.host)
    config.access_token = jwt_token
    api_client = ApiClient(config)

    exporter = Carbon3dCsvExporter(api_client)
    exporter.export_printed_parts(args.export_path, filter_options, args.sort_options, args.max_records)

if __name__ == '__main__':
    main()
