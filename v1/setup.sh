#!/bin/bash
DIR=`dirname "$0"`
SPEC_URL=${SPEC_URL:="https://api-sandbox.carbon3d.com/v1/api.yaml"}
SPEC_FILE="${DIR}/carbon-api-v1.yaml"
GEN_DIR="${DIR}/python/gen"

echo "Downloading ${SPEC_URL}..."
curl -s "${SPEC_URL}" --output "${SPEC_FILE}"

# Generate python api from spec
npx @openapitools/openapi-generator-cli generate \
  -i "${SPEC_FILE}" \
  -g python \
  -p packageVersion=1.0.0,projectName=carbon-sdk,packageName=carbon,library=urllib3 \
  -o "${GEN_DIR}"

# Install python api
pip3 install --user "${GEN_DIR}"
