import requests

puturl="https://api.restful-api.dev/objects/ff8081819782e69e019be4096d042e99"

body2={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}

r2=requests.put(puturl,json=body2)
print("put status code",r2.status_code)
print(r2.json())