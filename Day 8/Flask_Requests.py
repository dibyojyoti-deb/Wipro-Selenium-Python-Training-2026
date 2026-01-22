#GET
import requests
geturl="http://127.0.0.1:5000/users"

headers={
    "Accept":"application/json",
    "User-Agent":"Python-Requests-Client"

}

r=requests.get(geturl)
print ("get status code",r.status_code)
print(r.json())

#POST

posturl="http://127.0.0.1:5000/users"

body1={
  "name": "Preeti"
}

r1=requests.post(posturl,json=body1)
print("post status code",r1.status_code)
print(r1.json())

#PUT

puturl="http://127.0.0.1:5000/users/2"

body2={
  "name": "Rishi"
}
r2=requests.put(puturl,json=body2)
print("put status code",r2.status_code)
print(r2.json())

#PATCH
patchurl="http://127.0.0.1:5000/users/1"

body={
  "name": "Mohan"
}
r=requests.put(patchurl,json=body)
print("put status code",r.status_code)
print(r.json())

#DELETE
deleteurl="http://127.0.0.1:5000/users/1"

response=requests.get(deleteurl)

print("get status code",response.status_code)
print(response.json())