import random
rand_int= random.randint(1, 10)
a = int(input("input a number from 1-10: "))
x = []
while(a != rand_int):
    x.append(a)
    print("Incorrect, try again")
    if(a < rand_int):
        print("guess higher")
    else:
        print("guess lower")
    a = int(input("input a number from 1-10: "))
print("Correct, congratulations!")
print("List of geusses", x)