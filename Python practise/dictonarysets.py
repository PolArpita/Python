# creating a dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London",
  "fruits":[1,2,3,4],
  "anotherdict":{"arpita":'player'},

}
print(country_capitals)
print(country_capitals['anotherdict'])
country_capitals["fruits"]=[6,7,8,9] #update
print(country_capitals)
#methods
print(list(country_capitals.keys()))#gives keys
print(list(country_capitals.values()))#print values
print(list(country_capitals.items())) #print keys values for all contetns
updatedict={
    "appu":"riya"
}
country_capitals.update(updatedict)
print(country_capitals)
print(country_capitals.get(appu1)) #returns none as it is not present in a dict (pronts associated value)
print(country_capitals[appu1]) #throws an error



