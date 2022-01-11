# changed the values in this section of code:
x = [ [5,2,3], [15,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Bryant'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

# printed the proper formatting of the dictionary in this seciton of code:
def iterateDictionary(students):
  students = [
    {'first_name' :  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ]
  return students
name = iterateDictionary(students)

print(f"first_name - {name[0]['first_name']}, last_name - {name[0]['last_name']}")
print(f"first_name - {name[1]['first_name']}, last_name - {name[1]['last_name']}")
print(f"first_name - {name[2]['first_name']}, last_name - {name[2]['last_name']}")
print(f"first_name - {name[3]['first_name']}, last_name - {name[3]['last_name']}")

# printing all first and last names in this section of code:
# def iterateDictionary2(name):
#   for x in range(len(name)):
#     print(f"{name[x]['first_name']}")
# iterate = iterateDictionary(name)
# print(iterate)

print(f"{name[0]['first_name']}")
print(f"{name[1]['first_name']}")
print(f"{name[2]['first_name']}")
print(f"{name[3]['first_name']}")

print(f"{name[0]['last_name']}")
print(f"{name[1]['last_name']}")
print(f"{name[2]['last_name']}")
print(f"{name[3]['last_name']}")

# printing all of the locations and the instructors
location_num = 0 # I couldn't figure out how to get the location number to display properly when looping
instructor_num = 0

def printInfo(dojo,location_num,instructor_num):
  dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
  }

  print("-----------")
  print(f"7 LOCATIONS")
  for x in range(len(dojo['locations'])):
    location_num+=x
    print(f"{dojo['locations'][x]}")

  print("-----------")
  print(f"8 INSTRUCTORS")
  for x in range(len(dojo['instructors'])):
    instructor_num+=x
    print(f"{dojo['instructors'][x]}")    

  return dojo
dojo = printInfo(students,location_num,instructor_num)