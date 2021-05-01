
import json
# JvaScript Notation language
employee_data='''
{
"people":[
{
"Name":"Nilesh",
"Email":"nilesh@gmail.com",
"Marital":"Unmarid"
},
{
"Name":"lokesh",
"Email":"lokesh@gmail.com",
"Marital":"Unmarid"
}
]}
'''

print(employee_data)

data = json.loads(employee_data)
print(data)
# Python covert JSON format data into dictionary ie in key value pair format.

