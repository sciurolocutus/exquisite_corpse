#!/bin/bash
jwt=$1
curl -X POST "http://127.0.0.1:5000/corpora" -H "Content-Type: application/json" -H "Authorization: JWT ${jwt}" -d '{}'
