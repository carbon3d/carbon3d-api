# coding: utf-8

# flake8: noqa

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  A Carbon DLS API token ([JWT](https://en.wikipedia.org/wiki/JSON_Web_Token)) must be included with each request to the API.  Steps to create API tokens: - Create and download an API key [here](https://print.carbon3d.com/api_keys) - For testing: Generate JWT tokens using the [token generator](/token_generator) - For production: Generate JWT tokens dynamically (<em>see authtoken-create.py example</em>) - A valid Carbon API token must be included as <code>Authorization: Bearer [token]</code> HTTP header.  This API provides a programmatic interface for submitting part (and soon build) orders. The general process for creating an order is as follows:  - Upload model files to the API with the [/models](#/Models) endpoint - Create parts that reference a model and a part number with the [/parts](#/Parts) endpoint   -  Part numbers can be created [here](https://print.carbon3d.com/catalog_parts) - Create an order with the [/orders](#/Orders) endpoint  Uploaded models, parts and orders can be retrieved either in bulk or by UUID at the [/models](#/Models), [/parts](#/Parts) and [/orders](#/Orders) endpoints, respectively.  Once a part order is submitted, automatic packing will create one or more builds (for mass-customization applications only).  Builds can be retrieved either in bulk or by UUID at the [/builds](#/Builds) endpoint. - Build attachments (traveler, slice video) can be retrieved by UUID at the [/attachments](#/Attachments) endpoint.  This API also provides a programmatic interface to access [printer](#/Printers) (fleet) status and query for [prints](#/Prints).   # noqa: E501

    The version of the OpenAPI document: 0.0.4
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.0.4"

# import apis into sdk package
from carbon3d.api.attachments_api import AttachmentsApi
from carbon3d.api.builds_api import BuildsApi
from carbon3d.api.models_api import ModelsApi
from carbon3d.api.orders_api import OrdersApi
from carbon3d.api.parts_api import PartsApi
from carbon3d.api.printed_parts_api import PrintedPartsApi
from carbon3d.api.printers_api import PrintersApi
from carbon3d.api.prints_api import PrintsApi

# import ApiClient
from carbon3d.api_client import ApiClient
from carbon3d.configuration import Configuration
from carbon3d.exceptions import OpenApiException
from carbon3d.exceptions import ApiTypeError
from carbon3d.exceptions import ApiValueError
from carbon3d.exceptions import ApiKeyError
from carbon3d.exceptions import ApiException
# import models into sdk package
from carbon3d.models.build import Build
from carbon3d.models.build_attachments import BuildAttachments
from carbon3d.models.builds_response import BuildsResponse
from carbon3d.models.model import Model
from carbon3d.models.models_response import ModelsResponse
from carbon3d.models.order import Order
from carbon3d.models.order_request import OrderRequest
from carbon3d.models.order_request_parts import OrderRequestParts
from carbon3d.models.order_status import OrderStatus
from carbon3d.models.order_update_request import OrderUpdateRequest
from carbon3d.models.orders_response import OrdersResponse
from carbon3d.models.orders_response_orders import OrdersResponseOrders
from carbon3d.models.part import Part
from carbon3d.models.part_genealogy import PartGenealogy
from carbon3d.models.part_genealogy_build_info import PartGenealogyBuildInfo
from carbon3d.models.part_genealogy_print_info import PartGenealogyPrintInfo
from carbon3d.models.part_request import PartRequest
from carbon3d.models.parts_response import PartsResponse
from carbon3d.models.print_ref import PrintRef
from carbon3d.models.printed_part import PrintedPart
from carbon3d.models.printed_part_ref import PrintedPartRef
from carbon3d.models.printed_part_status import PrintedPartStatus
from carbon3d.models.printed_parts_response import PrintedPartsResponse
from carbon3d.models.printer import Printer
from carbon3d.models.printer_prints import PrinterPrints
from carbon3d.models.printer_status import PrinterStatus
from carbon3d.models.printers_response import PrintersResponse
from carbon3d.models.prints_response import PrintsResponse

