#!/opt/venvs/securedrop-app-code/bin/python

import sys

sys.path.insert(0, "/var/www/securedrop")

# import logging
# logging.basicConfig(stream=sys.stderr)

from source import app as application
