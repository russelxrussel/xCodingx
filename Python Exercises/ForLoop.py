"""
for Loop exercise 01.14.2019
"""

"""Display 10 times the i value
for i in range(10):
    print("Hello World", i)
"""


"""For Loop with user input
num_start = int(input("Please Enter number to start:"))
num_iterate = int(input("Please Enter number to iterate:"))
num_hop = int(input("Please Enter number to hop:"))
for i in range(num_start, num_iterate, num_hop):
    print("[",i,"]")

"""

fact = 1
num = int(input("Enter number: "))
for i in range(1, (num + 1)):
    fact = fact * i
    print (i,"is ", fact)
print(fact)
