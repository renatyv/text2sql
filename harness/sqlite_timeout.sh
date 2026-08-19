#!/bin/sh
exec /usr/bin/timeout "${BEAVER_QUERY_TIMEOUT:-10}s" /usr/bin/sqlite3 "$@"
