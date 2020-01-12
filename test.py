import requests


r = requests.get("https://rmotr.com")
print(r.status_code)
print(r.ok)

name = input("Your name? ")
print(f"Hello {name}")

