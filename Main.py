name=input("please enter your name: ")
yourage=input("enter your age: ")
age=int(yourage)

if not age > 20:
    print("unfortunately", name, "you are younger")
else:
    print(name, "you are older than 20 years old")
