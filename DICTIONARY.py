courses={1: 'python' , 2: 'data science' , 'third': 'machine learning'}     #dictionary (combination of keys and values)
print(courses)

print(courses['third']) #accessing key to fetch value

print(courses[1])   #accessing key to fetch value

print(courses.get(2)) #another methon to access key for fetching value

courses['third']='hadoop' #renaming the value

print(courses)

courses['four']='machine learning' #adding new record to dictionary

print(courses)
