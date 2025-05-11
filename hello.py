# hello.py
import requests

print("Hello from GitHub Actions!")
print("Status code from example.com:", requests.get("https://mbl.is").status_code)
