#!/bin/bash
corpus=1
if [[ ! -z "$1" ]]
	then corpus="$1"
fi
entry=1
if [[ ! -z "$2" ]]
	then entry="$2"
fi
curl "http://127.0.0.1:5000/corpora/${corpus}/entries/${entry}"
