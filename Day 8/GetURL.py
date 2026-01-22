import requests

#GET
geturl1="https://api.restful-api.dev/objects"

response=requests.get(geturl1)

print("get status code",response.status_code)
print(response.json())

geturl2="https://api.restful-api.dev/objects?id=3&id=5&id=10"

response=requests.get(geturl2)

print("get status code",response.status_code)
print(response.json())

geturl3="https://api.restful-api.dev/objects/7"

response=requests.get(geturl3)

print("get status code",response.status_code)
print(response.json())