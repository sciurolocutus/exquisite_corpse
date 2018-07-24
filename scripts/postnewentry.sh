#!/bin/bash
jwt=$1
corpus=1
if [[ ! -z "$2" ]]
	then corpus="$2"
fi
entry="entry.json"
if [[ ! -z "$3" ]]
	then entry="$3"
fi
curl -X POST "http://127.0.0.1:5000/corpora/${corpus}/entries" -H "Authorization: JWT ${jwt}" -H 'Content-Type: application/json' -d @${entry}
