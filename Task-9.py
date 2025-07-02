# Delete a list of keys from a dictionary
# # Keys to remove
# keys = ["name", "salary"]
sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
sample_dict.pop('name')
sample_dict.pop('salary')
print(sample_dict)


# 2. Count the frequency of each character in a given string using a dictionary.
x="python developers"
d={}
for i in x:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)


# 3. Swap keys and values in a dictionary.
h={'a':1,'b':2,'c':3,'d':5}
d={}
for i,j in h.items():
    d[j]=i
print(d)

# 4. Write a program to sum all the values in a dictionary.
h={'a':1,'b':2,'c':3,'d':5,'e':6}
sum=0
for i in h:
    sum+=h[i]
print(sum)
    

# 5. Create a nested dictionary for student details (name, roll, marks).
d={"student-1":{'name':"Ajay",'Roll':12,'marks':90},
    "student-2":{'name':"Ram",'Roll':30,'marks':88},
    "student-3":{'name':"krish",'Roll':28,'marks':96}}
print(d)

# 6. Convert a dictionary to a list of tuples.
h={'a':1,'b':2,'c':3,'d':5,'e':6}
for i in h.items():
    print(i)

# 7. Write a program to store names as keys and their lengths as values.
k=['programming','Languages','developers']
l=[6,7,8]
d={}
for i in k:
   d[i]=len(i)
print(d)

# 8. Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and 
# "odd" if the number is odd
# Expected Output:
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
d={}
for i in range(1,6):
    if i%2==0:
        d[i]="even"
    else:
        d[i]="odd"
print(d)

# 9. Create Reverse Word Dictionary
# Given list of words: Create a dictionary with words as keys and their reversed strings as values
# Expected Output:
# {'cat': 'tac', 'dog': 'god', 'bat': 'tab'}

words = ["cat", "dog", "bat"]
d={}
for i in words:
    res=""
    for j in i:
        res=j+res
    d[i]=res
print(d)


