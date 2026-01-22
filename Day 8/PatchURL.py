import requests

patchurl="https://api.restful-api.dev/objects/ff8081819782e69e019be4096d042e99"

body={
   "name": "Apple MacBook Pro 16 (Updated Name)"
}
r=requests.put(patchurl,json=body)
print("put status code",r.status_code)
print(r.json())