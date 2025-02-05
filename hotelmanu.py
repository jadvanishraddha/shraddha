manu = {
    'kadhi':"rs40",
    'rotlo':20,
    'khichdi':35,
    'sambhar':25,
    'idli':15,
}

print("welcome to shree krishna restaurant")
print(manu)

A = 0

i1 = input("enter the name of iten you want to order =")
if i1 in manu:
    A += manu[i1]
    print(f"your item {i1} is added to your order")

else:
    print(f"ordered item {i1} is not available yet!! ")


B = input("do you want to add another item? (yes/no)")
if B == "yes":
    i2 = input("enter the name of secind item = ")
    if i2 in manu:
        A += manu[i2]
        print(f"your item {i2} is added to your order")

    else:
        print(f"orderd item {i2} is not available yet!!")

print(f"totle amount of item to pay is {A}")
