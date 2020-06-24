# Python Carbon3d API Client

### Installation
To install the [carbon3d python client](https://pypi.org/project/carbon3d-client/), just run:
`pip3 install carbon3d-client pyjwt`

### Generating an access token
First, generate an API key and download the secret.json file by following the steps at https://carbon3d.print.carbon3d.com/api_keys

You can then create your access token using the example script `authtoken-create.py`
```
# generate an access token that is valid for 24 hours
v1/python_examples/authtoken_create.py path/to/secret.json --exp_minutes 1440
```

### Create a custom part order
This API provides a programmatic interface for submitting part (and soon build) orders. The general process for creating an order is as
1. Upload model files to the API with the /models endpoint
2. Create parts that reference a model and a part number with the /parts endpoint (Part numbers can be created here too)
3. Create an order with the /orders endpoint

Uploaded models, parts and orders can be retrieved either in bulk or by UUID at the /models, /parts and /orders endpoints, respectively. 

Once a part order is submitted, automatic packing will create one or more builds (for mass-customization applications only).

Builds can be retrieved either in bulk or by UUID at the /builds endpoint.

Build attachments (traveler, slice video) can be retrieved by UUID at the /attachments endpoint.

```
./v1/python_examples/custom_part_order.py --help
usage: custom_part_order.py [-h] [--application_id APPLICATION_ID]
                            [--host HOST] --part_catalog_num PART_CATALOG_NUM
                            --order_number ORDER_NUMBER --due_date DUE_DATE
                            --secret SECRET
                            files [files ...]

Script to upload models, create parts, and create an order

positional arguments:
  files                 Model file paths (.stl)

optional arguments:
  -h, --help            show this help message and exit
  --application_id APPLICATION_ID, -a APPLICATION_ID
                        Application scope for part number (default: 0)
  --host HOST           Carbon API host (default: https://api.carbon3d.com/v1)
  --part_catalog_num PART_CATALOG_NUM, -p PART_CATALOG_NUM
                        Part catalog number i.e. ALIGNER-001 (default: None)
  --order_number ORDER_NUMBER, -o ORDER_NUMBER
                        Order number (default: None)
  --due_date DUE_DATE, -d DUE_DATE
                        Number of days from today for order due date to be set
                        (default: None)
  --secret SECRET, -s SECRET
                        JSON file with client_id and client_secret (default:
                        None)
```
