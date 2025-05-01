#Create an dictionary
person ={
    "Name": "Nike",
    "Age": 22,
    "City": "New York"
}
#Accessing values using key
print("Name of this person:",person["Name"])
print("Age of this person:",person["Age"])
print("Location of this person:",person["City"])
#Accessing through loop
for key, value in person.items():
    print(key, ":", value)


