import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)

r = requests.get("https://rmotr.com")
print(r.status_code)

name = input("Your name? ")
print(f"Hello {name}")

