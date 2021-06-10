#Import the library and open the file you will write to. You also create the Faker
#`object

from faker import Faker
import json

output=open('data.JSON','w')
fake = Faker()

#create 1000 records, so you will need to create a dictionary to hold the data. 
#After creating a dictionary to hold the records, add a 'records'  key and initialize it with a blank array.

alldata={}
alldata['records']=[]

#To write records, you use Faker to create a dictionary , then append it to the array

for x in range(1000):
    data={"name":fake.name(),"age":fake.random_int(min=18, max=80, step=1),"street":fake.street_address(),"city":fake.city(),
            "zip":fake.zipcode(),"lng":float(fake.longitude()),"lat":float(fake.latitude())}
    alldata['records'].append(data)

#Lastly to write the JSON to a file, use the JSON.dump() method. 
#Pass the data that you want to write and file to write to.

json.dump(alldata,output)


#You now have a data.JSON file that has an array with 1,000 records. You can read this
#file by taking the following steps:

#Open the file using the following:
with open("data.JSON","r") as f:

#Use JSON.load() and pass the file reference to the method

    data=json.load(f)

#Inspect the json by looking at the first record using the following 
    data['records'][0]

#Or just use the name :
    data['records'][0]['name']


