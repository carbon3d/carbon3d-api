# Table of Contents
1. [Getting Started](#getting-started)
2. [Authentication](#authentication)
3. [Versioning and Updates to the API](#versioning-and-updates-to-the-api)
4. [API Rate Limits](#api-rate-limits)
5. [Examples](#examples)
6. [Feedback](#feedback)

## Getting Started
Welcome to the Carbon DLS API. The documentation here will help you get started integrating with our API. **Note that Carbon must grant access for you to begin your integration. Please contact your Business Development Director or support@carbon3d.com if you do not yet have access.**

The Carbon DLS API is a REST API that is built to enable outside systems to access specific information. The primary functions of the API include (a) offering access to near real-time printer and print status information and (b) enabling automatic design and print preparation actions.

The documentation is intended to help you get started and provide some examples, but detailed documentation about each request can be found at [https://api.carbon3d.com/v1/api-docs/#/](https://api.carbon3d.com/v1/api-docs/#/). Note that while examples are provided in Python, the REST API itself is language-agnostic.

## Authentication
The Carbon API uses a [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token) token to authenticate each request. Follow these steps to get started.
1. Generate an API Key [here](https://print.carbon3d.com/api_keys)* by clicking the "Create Authentication Key" button. This will automatically download a `secrets.json` file; your client secret is NOT stored by Carbon.
    1. Note: You must be an ADMIN user within your customer profile to access the API keys. You also need to remain ADMIN in order to use the API keys to authenticate with the API
2. You can now use the `v1/python_examples/authenticate-create.py` script to generate a valid token with your desired expiration. You can re-generate as many tokens as you'd like with new expirations utilizing the same secret. For example, to generate a token that is valid for 24 hours you could run:
    ``` bash
    v1/python/examples/authtoken-create.py path/to/secret.json --exp_hours 24
    ```
3. You must now add an HTTP header `Authorization: Bearer [token]` in all of your requests.

* **Please contact your Business Development Director or support@carbon3d.com if you cannot access API key management.**

## Versioning and Updates to the API
Please note that the CarbonAPI is confinually improving and that updates will be pushed out on a regular basis. Release notes can be found in [Carbon Acadamy](https://learn.carbon3d.com/software). Once in Carbon Acadamy, select "Content" then "Release Notes" in the drop down. From here you will be able to see all of the API release notes. Contact your Business Development Director or support@carbon3d.com if you cannot access API release notes on Carbon Academy.

When an update to the API is rolled out, the version will be updated. The following versioning protocol is followed:
* Patch version (eg. 0.1.2 -> 0.1.3): Small updates that do not require a client update.
* Minor version (eg. 0.1.2 -> 0.2.0): Client update required. Please update the carbon3d-client on your system to ensure proper integration with the API.
* Major version (eg. 0.1.2 -> 1.0.0): Client update required. Please update the carbon3d-client on your system to ensure proper integration with the API. Please note that this update is not backwards compatible and requires the latest software to run.

## API Rate Limits
To manage the amount of total requests that the API, please note that there is a rate limit of 200 requests per 10 seconds that is imposed on a per user level. If these rate limits are not adequate for your workflow, please contact your Business Development Director or support@carbon3d.com to discuss options.

## Examples
Python sample code is provided as a reference and starting point. While you may choose to use another language, the general workflow and guidelines for interacting with API data remain much the same.
Overviews of common tasks like [pagination/cursor use](v1/python_examples/README.md#pagination--cursor), [creating part orders for automated print preparation](v1/python_examples/README.md#create-a-custom-part-order), and more can be found in the [readme](v1/python_examples/README.md)

### Python
Several Python examples of common API transactions can be found in (v1/python_examples). These are ready to use, but are not intended to be complete solutions for interacting with production data.
Read more about our Python examples [here](v1/python_examples/README.md).

## Feedback
Please send all questions and feedback to <api-list@carbon3d.com>.
