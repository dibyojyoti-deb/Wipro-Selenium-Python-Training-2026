import requests

deleteurl="https://api.restful-api.dev/objects/6"

response=requests.get(deleteurl)

print("get status code",response.status_code)
print(response.json())