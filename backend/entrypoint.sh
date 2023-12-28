#!/bin/sh

exec python3 db.init.py &
exec "$@"
