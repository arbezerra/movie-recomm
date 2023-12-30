#!/bin/sh

python3 db.init.py &
job=$!
wait $job
"$@"
