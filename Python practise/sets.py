#a={} this creates empty dict not empty set
#not changable,not accessible

a={1,2,3,4,5}
print(type(a))
#emptyset below syntax
b=set() 
b.add(4)
b.add(5)
b.add(6)
b.add(4) # adding value repeatedly not change the set
print(b)
b.add((3,8,9))
print(b) # we can add tupl in set but not list not dictonary
print(len(b))
b.remove(5)
print(b)
print(b.pop()) #removes random element