# name=input("Enter your name\n:-")
# print("Good afternoon, "+name)
# letter='''Dear <|name|>,
# you are selected!
# Date: <|Date|>
# '''
# name=input("enter your name\n")
# date=input("enter date\n")
# letter=letter.replace("<|name|>",name)
# letter =letter.replace("<|Date|>",date)
# print(letter)

# detect double spaces in a string and replaces
st="this i a double space  program"
print(st.find("  ")) #if yes then reurn index if not then return -1
print(st.replace("  "," "))
