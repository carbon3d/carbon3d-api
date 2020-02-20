# Carbon API examples

## Requirements

- python3 (> 3.5) for python examples

## Installation

`pip install carbon3d-client`

## Running examples

### Model upload example

```
v1/examples/model-upload.py -h
usage: model-upload.py [-h] --model_id MODEL_ID --part_number PART_NUMBER
                       --access_token ACCESS_TOKEN [--url URL]
                       file

positional arguments:
  file                  model file

optional arguments:
  -h, --help            show this help message and exit
  --model_id MODEL_ID, -m MODEL_ID
  --part_number PART_NUMBER, -p PART_NUMBER
  --access_token ACCESS_TOKEN, -t ACCESS_TOKEN
                        JWT Access Token
  --url URL, -u URL     Carbon API URL prefix
```

### Model list example

```
v1/examples/model-list.py -h
usage: model-list.py [-h] [--model_id MODEL_ID] [--part_number PART_NUMBER]
                     --access_token ACCESS_TOKEN [--api API]

optional arguments:
  -h, --help            show this help message and exit
  --model_id MODEL_ID, -m MODEL_ID
                        API URL prefix
  --part_number PART_NUMBER, -p PART_NUMBER
  --access_token ACCESS_TOKEN, -t ACCESS_TOKEN
                        JWT Access Token
  --api API, -a API     API URL prefix
```

### Order creation example

```
usage: order-create.py [-h] --part_number PART_NUMBER --order_id ORDER_ID
                       --access_token ACCESS_TOKEN [--api API]
                       [model_id [model_id ...]]

positional arguments:
  model_id              model identifier

optional arguments:
  -h, --help            show this help message and exit
  --part_number PART_NUMBER, -p PART_NUMBER
  --order_id ORDER_ID, -o ORDER_ID
  --access_token ACCESS_TOKEN, -t ACCESS_TOKEN
                        JWT Access Token
  --api API, -a API     API URL prefix
```

## TODO

### Builds

### Parts
