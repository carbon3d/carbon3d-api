#!/bin/bash
DIR=`dirname "$0"`
SPEC_FILE="${DIR}/api.yaml"
GEN_DIR="${DIR}/generated"
VERSION=`head ${SPEC_FILE} | grep 'version: ' | awk '{ print $2 }'`

rm -rf ${GEN_DIR}

if [ -z "${VERSION}" ]; then
  echo "Could not find version"
  exit 1
fi

# Generate python api from spec
npx @openapitools/openapi-generator-cli generate \
  -i "${SPEC_FILE}" \
  -g python \
  -p packageVersion=${VERSION},projectName=carbon3d-client,packageName=carbon3d,library=urllib3 \
  -o "${GEN_DIR}"

