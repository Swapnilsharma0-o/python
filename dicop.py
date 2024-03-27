d = { 'name' : 'om','no' : 5444}
# print(d)

# r = dict([('collage','pbg' ), ('course',['it','cs','entc'])])
# print(r)

# d={}
# no_items = int(input("Enter no of items you wanto addd"))
# for i in range(0,no_items,1):
#     key = input("Enter keys")
#     values = input("enter values")
#     d[key]=values

# print(d)

# d={}
# keys = input("enter comma seperated keys:  ").split(",")
# values = input("enter comma seperated values:  ").split(",")
# for i in range(0,len(keys)):
#     d[keys[i]]=values[i]

# print(d)


# d= {'employee_id': 100, 'address': ['pune', 'maharastra']}
# print("The employee id is " , d['employee_id'])
# print("The employee id1 is " , d['address'])

# print("The employee id is " , d.get('employee_id'))
# print("The employee id1 is " , d.get('employee_id1'))
# print("The employee id1 is " ,d.get("employee_id1","Default_value"))

d= {'employee_id': 1000, 'address': ['pune', 'maharastra']}
# print(d.items())
# for key,value in d.items():
#     print(f'The {key} is {value}')   

d.update({'employee_id1': 1001, 'address1' : 'nashik' })
# print(d)

# d.update({'employee_id2' :1002})
# # print(d)
# print(d.items())
# del d['address']
# print(d.items())


d|= {"id":39} 
print(d)
     
d.update( {"id":99}  )
print(d)





























