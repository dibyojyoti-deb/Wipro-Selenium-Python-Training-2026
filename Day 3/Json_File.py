import json
 
data ={
    "Name":"Bhanu",
    "Age":"25",
    "Location":"Hyderabad",
    "Skills":['Java', 'Python']
}
 
with open("data.json", 'w') as file:
    json.dump(data, file, indent=4)
 