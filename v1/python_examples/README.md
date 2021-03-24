# Python Carbon3d API Client

## Table of Contents
- [Python Carbon3d API Client](#python-carbon3d-api-client)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Generating an access token](#generating-an-access-token)
  - [Getting Started](#getting-started)
  - [Filtering](#filtering)
  - [Total Count](#total-count)
  - [Sorting](#sorting)
  - [Pagination / Cursor](#pagination--cursor)
    - [Pagination](#pagination)
    - [Cursor](#cursor)
  - [Retrieving Quality Information](#retrieving-quality-information)
  - [Create a custom part order](#create-a-custom-part-order)
  - [Joining information from multiple endpoints](#joining-information-from-multiple-endpoints)
  - [Frequently Asked Questions](#frequently-asked-questions)

## Installation
To install the [carbon3d python client](https://pypi.org/project/carbon3d-client/), just run:
`pip3 install carbon3d-client pyjwt[crypto]`
Examples depend on additional packages that can be installed with:
`pip3 install pandas numpy`
*Note: The python examples here require Python 3.0 and above*

### Updating carbon3d-client
As the CarbonAPI is continually improving, there may be times when a client version update is required, just run:
`pip3 install carbon3d-client pyjwt[crypto] --upgrade`

To verify that the correct client is being used, just run:
`pip3 show carbon3d-client`

*Note that the version should match the version indicated at https://api.carbon3d.com/v1/api-docs/ .*


## Generating an access token
First, generate an API key and download the secret.json file by following the steps at https://print.carbon3d.com/api_keys. This file contents will resemble this:

```json
{
 "client_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 "client_secret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

There is a convenient script (`authtoken-create.py`) that takes in the path to your `secrets.json` file and some expiration time frame then prints out an authentication token.
```bash
# generate an access token that is valid for 24 hours
v1/python_examples/authtoken_create.py path/to/secret.json --exp_minutes 1440
```

## Getting Started
Start the script by importing the carbon package and setting the configuration.
```python
import carbon3d as carbon
import jwt
import json
import time

jwt_contents = {
    'iss': your_client_id_from_secrets_json,
    'exp': int(time.time() + 5 * 60) # Token will expire in 5 minutes
}
encoded_jwt = jwt.encode(jwt_contents, your_client_secret_from_secrets_json, algorithm='RS256')

config = carbon.Configuration(host='https://api.carbon3d.com/v1')
config.access_token = encoded_jwt.decode('utf-8')
```

Next prepare the API clients, each resource gets its own client.
```python
api_client = carbon.ApiClient(config)
printers_api = carbon.PrintersApi(api_client)
prints_api = carbon.PrintsApi(api_client)
```

From here you can make API calls directly using the clients.
```python
printers_response = printers_api.get_printers(limit=50, offset=0)
printers = printers_response.printers
prints = prints_api.get_prints(limit=100).prints
```

## Filtering
The API provides some basic filtering capabilities to allow you to access the data you need. This is NOT intended to facilitate complex queries to explore your data, you are encouraged to load data into your own database for those needs.

Querying with no filters is easy.
```python
prints_api = carbon.PrintsApi(api_client)
all_prints = prints_api.get_prints(limit=100)
```

If you want to query for all prints that used platform `1A0000`
```python
filtered_prints = prints_api.get_prints(limit=100, platform_serial="1A0000")
```

As of 08/11/2020 Carbon is still in the process of updating all of the filters to support requesting arrays. This is NOT yet implemented for all endpoints. Please check [https://api.carbon3d.com/v1/api-docs/#/](https://api.carbon3d.com/v1/api-docs/#/) for up to date information on filter options available for each endpoint. The following would return all prints that were printed with platform `1A0000` OR platform `1B0000`.
```python
filtered_prints = prints_api.get_prints(limit=100, platform_serial=["1A0000", "1B0000"])
```

Combining two different filters will always result in an `AND` query. The API currently does not support `OR` queries. The following will return prints on printer `1C0000` that utilized the platform `1A0000`.
```python
filtered_prints = prints_api.get_prints(limit=100, platform_serial="1A0000", printer_serial="1C0000")
```

For date ranges you can use the `_after` or `_before` query parameters. For example, here is how to query all prints that started since yesterday.
```python
from datetime import date, timedelta
yesterday = date.today() - timedelta(days=1)
filtered_prints = prints_api.get_prints(limit=100, started_after=yesterday)
```

The API currently only supports exact matches, no wildcard queries or `LIKE` queries are supported.

## Total Count
The API will return an accurate total count of the results of your query up to 10,000 results. If you have more than 10,000 results for your query it will continue to return a `total_count` of 10,000. There is no existing method for retrieving an accurate total count of resources with >10,000 records.

## Sorting
You can sort by one or multiple fields. It is recommended you make no assumptions about the default sorting, if you would like to guarantee a particular order then explicitly provide the sort parameter.

The default will assume you want to sort in ascending order.
```python
part_orders_api = carbon.PartOrdersApi(api_client)
part_orders_api.get_part_orders(limit=100, sort=["due_date"])
```

You can also sort by multiple values. The following will sort be part_order_number in descending order then by due_date in ascending order.
```python
part_orders_api.get_part_orders(limit=100, sort=["part_order_number,desc", "due_date"])
```

As of 08/11/2020 Carbon is still the process of adding sorting functionality to all list endpoints. This is NOT yet implemented for all endpoints. Please check [https://api.carbon3d.com/v1/api-docs/#/](https://api.carbon3d.com/v1/api-docs/#/) for up to date information on filter options available for each endpoint.

## Pagination / Cursor
As of 12/22/2020 All endpoints except 'printers' are using the cursor implementation. Please check [https://api.carbon3d.com/v1/api-docs/#/](https://api.carbon3d.com/v1/api-docs/#/) for up to date information..


### Pagination
Retrieving the first page of data is as simple as setting the limit and offset to their default values of 100 and 0 respectively.
```python
printers = printers_api.get_printers(limit=100, offset=0)
```

To get the next set of results you would increment the offset by 1.
```python
printers = printers_api.get_printers(limit=100, offset=1)
```

To check if you have retrieved all the data you can check if the number of results is less than the limit.
```
is_last_page = printers.limit > len(printers.printers.length)
```


### Cursor
Nothing but the limit needs to be set the first time you query.
```python
prints = prints_api.get_prints(limit=100)
```

The response to your first query will include a value for `next_cursor` which you can use to query for your next set of results.
```python
prints = prints_api.get_prints(limit=100, cursor=prints.next_cursor)
```

In order to use the cursor effectively it is recommended you:
1. Do not change any query parameters including filtering, sorting, etc. between the request that provided the `next_cursor` and the request where you are using the `cursor`
2. Do not use the `next_cursor` more than 1 minute after the API has provided it i.e. the next_cursor expires in 60 seconds.

Even following these rules, you may encounter duplicates or missing records if data was updated throughout your various queries to retrieve data. For example, if you query for `prints` sorted by `updated_at,desc`, your first query may retrieve all `prints` that were updated between now and 1 hour ago. Your next query will attempt to only find you records that were updated more than an hour ago. If one of your old print records is updated AFTER your first query, it will never be returned as when you made the first query it hadn't been updated in a while and when you made your second query it had just been updated.

You will need to reconcile these discrepancies but there are a few best practices.
1. If sorting on `updated_at` always sort in `ascending` order so that records that updated between queries are duplicated rather than missing entirely.
2. Use the `uuid` of a resource to properly de-duplicate; this will always be unique and the most recent query is the source of truth for that `uuid`.
3. Do not use a `cursor` more than 60 seconds after it was returned.


## Retrieving Quality Information
Before retrieving the actual measurements, it's important to retrieve the measurement templates so you can understand what the individual measurements represent.

```python
part_measurement_template_api = carbon.PartMeasurementTemplatesApi(api_client)
results = part_measurement_template_api.get_part_measurement_templates(limit=100)
```

The following is a hypothetical measurement template as if you just ran: `print(results.part_measurement_templates[0])`
```json
{
  "uuid": "11111111-1111-1111-1111-111111111111",
  "updated_at": "2020-01-08T00:00:00.000Z",
  "production_sop_name": "Widget ABC",
  "production_sop_version": 1,
  "operation_name": "Quality Control",
  "measurement_name": "Weight",
  "zones": [],
  "zones_enabled": false,
  "required_level": "required",
  "measurement_type": "value",
  "units": "g",
  "min": 100,
  "max": 110,
  "measurement_classification": "mass",
  "category_options": null
}
```
All of this information was manually configured in the cloud quality management system. Once you have a mapping of all the measurement templates, querying the part measurements API will make a lot more sense.

```python
part_measurements_api = carbon.PartMeasurementsApi(api_client)
results = part_measurements_api.get_part_measurements(limit=100)
```

The following is a hypothetical measurement as if you just ran: `print(results.part_measurements[0])`
```json
{
  "uuid": "33333333-3333-3333-3333-333333333333",
  "printed_part_uuid": "22222222-2222-2222-2222-222222222222",
  "part_measurement_template_uuid": "11111111-1111-1111-1111-111111111111",
  "value": 105,
  "category_value": "",
  "updated_at": "2020-01-08T00:00:00.000Z",
  "measurement_result": "pass",
  "zones": [],
  "notes": ""
}
```
Note how the `part_measurement_template_uuid` matches the `uuid` you saw in the request to `part_measurement_templates`. The measurement you are looking at is a `Weight` measurement with specs ranging from `100` to `110` and it was measured in `grams`.


## Create a custom part order
This API provides a programmatic interface for submitting part orders. The general process for creating an order is as follows:
1. Upload model files to the API with the /models endpoint
2. Create parts that reference a model and a part number with the /parts endpoint
3. Create an order with the /part_orders endpoint

Part orders can be created with an optional `build_sop_uuid` parameter, which references a Build SOP that configures automatic build generation. Generated builds will only contain parts from orders with the same Build SOP.
Manage at https://print.carbon3d.com/build_sops

Part orders can be grouped with an optional `packing_group` parameter, a string to identify part orders that should only be processed together. Part orders with different packing groups will be processed into different builds. Part orders with an unspecified packing_group will be treated as a separate group and will be packed together. A maximum of 40 total concurrent packing groups are permitted for 'open' and 'processing' PartOrders (contact carbon at api-support@carbon to increase this limit).

Once a part order is submitted, automatic packing will create one or more builds with the parts within the part order (for mass-customization applications only). Currently, the maximum number of parts that will be placed on a build is 35.

Uploaded models, parts and orders can be retrieved either in bulk or by UUID at the /models, /parts and /part_orders endpoints, respectively.

Builds can be retrieved either in bulk or by UUID at the /builds endpoint.

Build attachments (traveler, slice video) can be retrieved by UUID at the /attachments endpoint.

```bash
./v1/python_examples/custom_part_order.py --help
usage: custom_part_order.py [-h] [--application_uuid APPLICATION_UUID]
                            [--host HOST] --part_catalog_num PART_CATALOG_NUM
                            --part_order_number PART_ORDER_NUMBER --due_date DUE_DATE
                            --secret SECRET
                            files [files ...]

Script to upload models, create parts, and create an order

positional arguments:
  files                 Model file paths (.stl)

optional arguments:
  -h, --help            show this help message and exit
  --application_uuid APPLICATION_UUID, -a APPLICATION_UUID
                        Application scope for part number (default: 0)
  --host HOST           Carbon API host (default: https://api.carbon3d.com/v1)
  --part_catalog_num PART_CATALOG_NUM, -p PART_CATALOG_NUM
                        Part catalog number i.e. ALIGNER-001 (default: None)
  --part_order_number PART_ORDER_NUMBER, -o PART_ORDER_NUMBER
                        Part order number (default: None)
  --due_date DUE_DATE, -d DUE_DATE
                        Number of days from today for order due date to be set
                        (default: None)
  --secret SECRET, -s SECRET
                        JSON file with client_id and client_secret (default:
                        None)
```

## Joining information from multiple endpoints
In order to reduce the payload of a response, only specific information is returned from each endpoint, but you can combine responses from different endpoints to join data.

For example, for a given model or set of model names, in order to get the respective printed part status, combine the following calls:

Retrieve the desired model uuids:

```python
models_api = carbon.ModelsApi(api_client)
models_request = models_api.get_models(limit=10)
```

For the given set of model uuids, retreive the part uuids:

```python
parts_api = carbon.PartsApi(api_client)
parts_request = parts_api.get_parts(model_uuid=[x.uuid for x in models_request.models], limit=5)
```

With the given part uuids, retrieve the respective printed part information:

```python
printed_parts_api = carbon.PrintedPartsApi(api_client)
printed_parts_request = printed_parts_api.get_printed_parts(part_uuid=[x.uuid for x in parts_request.parts], limit=5)
```

Within the printed part response includes the status information regarding the specified models:

```json
 {"build_uuid": "",
            "error": None,
            "model_uuid": "11111111-1111-1111-1111-111111111111",
            "part_number": "113080-01",
            "part_order_number": "",
            "part_order_uuid": "",
            "part_uuid": "22222222-2222-2222-2222-222222222222",
            "print_id": "ABC12345",
            "print_order_number": "",
            "print_order_uuid": "33333333-3333-3333-3333-333333333333",
            "serial_number": "KTJ00BBA-14",
            "status": "complete",
            "tags": {"part": None,
                     "part_number": None,
                     "printed_part": {}},
            "uuid": "44444444-4444-4444-4444-444444444444"}
```
## Frequently Asked Questions
### What is an application id?
You can think of an Application as a shareable folder for models, parts, projects, etc. that are related to each other. You might have one Application for a running shoe midsole you are working on and another Application for face shields. Functionality to share and manage your applications hasn't been exposed yet, so if you think you want to change how your applications are set up please reach out to your Carbon Technical Partner.

### What's the difference between a model and a part?
Models can't be printed; they just represent three-dimensional shapes that can be used in a variety of parts. For example, you could have a model for an iPhone case that is used in 2 parts, one that is printed in EPU 41 and another in UMA 90.

### Can I specify how my parts are packed onto a build for a given part order?
The automatic packer currently has a set of predefined rules that specify how a build should be assembled. These rules are currently tuned for mass customized parts of similar geometry. Please let us know if you'd like to have the functionality to adjust these rules through the API by reaching out to <api-list@carbon3d.com>.

### Where can I find the build(s) generated from requesting a part order?
The builds created from a given part order can be found in Builds Catalog under the Production tab at print.carbon3d.com. The name of the build will be AutoBuildXXX. By selecting the desired build in this UI, you will be able to also see the build_uuid and other relevant information. (*Note this information is also returned when querying the /builds endpoint.*) You can queue the given build to a printer from the Build Catalog to a printer in your fleet.


### What's the difference between a project and a build?
A project is a collection of builds that have been modified over time. For example, let's say you open our project editing software, upload 10 models, then click print. Afterwards, you realize you want to change the orientation of a few of the models so you open the project again, modify the orientation, and click print. You printed the same project but two different builds.

### How can I queue a build?
You can use the [createPrintOrder](https://api.carbon3d.com/v1/api-docs/#/PrintOrders/createPrintOrder) API method.

### Why can't I see my models, orders, etc. in the UI.
Please let us know if you'd like to see these concepts exposed in our UI by reaching out to <api-list@carbon3d.com>.

### What is a part number?
Part numbers are a common term used in manufacturing to denote a reference to a particular _part design_. Each company chooses their own conventions for assigning part numbers, but generally a single part number is capable of having multiple versions or revisions. It is important to understand that a part number identifies a part _design_, whereas a serial numbers is a unique identifier for _a particular instantiation_ of that part design.

### Are there any API calls that allow me to interact with the printer (e.g. start a print, open the door, etc)?
This API is not intended to facilitate robotic automation for a printer. If this is something you need, please let your Carbon Technical Partner know.

### Can you add ____ to the print data we are able to export?
We would love to hear from you; please submit the request via <api-list@carbon3d.com>.