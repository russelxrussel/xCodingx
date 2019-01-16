#For Loop with For Loop Nested

user_input = int(input("Please enter a number: "))
i = 1
j = 1
for i in range(user_input):
    print (user_input * i)
    while(user_input < 10):
        print ("----")
        print (user_input * j)
        j = j + 1
