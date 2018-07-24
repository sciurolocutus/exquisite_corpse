#!/bin/bash
jwt=$1
curl -X POST "http://127.0.0.1:5000/corpora/1/entries" -H "Authorization: JWT ${jwt}" -H 'Content-Type: application/json' -d @entry.json
