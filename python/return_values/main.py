# Return function


def input_userdata():
    name=input("Please enter your name: ")
    age= int(input("Please enter your age : "))
    return name,age
    

user_name = input_userdata()

print(user_name[0])
print(user_name[1])