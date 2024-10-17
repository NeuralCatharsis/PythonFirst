x=int(input("Please enter an integer:\n"))
y=int(input("Please enter an integer:\n"))
res=x+y
print(f"The add sum of {x} and {y} is {res}")
if (res>5):
    print(f"{res} is bigger than 5")
elif (res<5):
    print(f"{res} is smaller than 5")
else:
    print("Nothing")