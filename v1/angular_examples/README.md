# Getting started

## API Auth Proxy
This proxy server generates short-lived API tokens from a client key /secret file and adds the required Authorization header.

Obtain API secrets at https://carbon3d.print.carbon3d.com/api_tools and save the secrets file.

Install required node modules:

```
cd v1/angular_examples
npm i
```

Launch proxy:

```
node ./api-proxy.js <secrets-file>
```

To test, you can view printer status at http://localhost:4200/api/v1/printers?limit=10&offset=0

## Simple angular demo
This demo app uses the auth proxy to show printer status.

In a second shell:
```
# generate angular models and services from API
npm install -g ng-openapi-gen
cd v1/angular_examples/printer-status/src
ng-openapi-gen --input https://api.carbon3d.com/v1/api.yaml --output ./api

# install dependencies
npm i

# run app
npm start
```

View http://localhost:4200/
