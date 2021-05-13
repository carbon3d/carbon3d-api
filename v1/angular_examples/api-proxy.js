/*
  Carbon API proxy service
  - Usage: node api-proxy.js <secrets file>
 */

/**
 * Module dependencies.
 */
const express = require('express');
const path = require('path');
const {createProxyMiddleware} = require('http-proxy-middleware');
const jwt = require('jsonwebtoken');

function loadKey(path) {
  try {
    return require(path);
  } catch (err) {
    console.error(err);
    process.exit(1);
  }
}

const args = process.argv.slice(2);
const keyFilePath = args[0];
if (!path) {
  console.error('Usage: node api-proxy.js <secrets file>')
}
const {client_id, client_secret} = loadKey(keyFilePath);

console.log('>> Using Carbon API secrets at', keyFilePath);

function getToken(expMinutes = 1) {
  const tokenContent = {
    iss: client_id,
  };
  return jwt.sign(tokenContent, client_secret, {
    algorithm: 'RS256',
    expiresIn: expMinutes * 60 * 60 * 1000,
    mutatePayload: true,
  });
}

/**
 * Configure proxy middleware
 */
const carbonApiProxy = createProxyMiddleware({
  target: 'https://api.carbon3d.com',
  changeOrigin: true, // for vhosted sites, changes host header to match to target's host
  logLevel: 'debug',
  "pathRewrite": {
    "^/api": ""
  },
  onProxyReq: function (proxyReq) {
    proxyReq.setHeader('Authorization', 'Bearer ' + getToken())
  }
});

const app = express();

/**
 * Add the proxy to express
 */
app.use('/api', carbonApiProxy);

app.listen(4088);

console.log('[PROXY] Server: listening on http://localhost:4088');
console.log('[PROXY] Server: printer status on http://localhost:4088/api/v1/printers?limit=1&offset=0');

