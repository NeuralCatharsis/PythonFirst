choice=int(input("Choose desired operator.\n Enter 1 for (+) Addition\n Enter 2 for (-) Subtraction\n Enter 3 for (×) Multiplication\n Enter 4 for (÷) Division\n"))
if choice==1:
    x=int(input("Please enter an integer:\n"))
    y=int(input("Please enter an integer:\n"))
    res=x+y
    print(f"{x}+{y}={res}")

elif choice==2:
    x=int(input("Please enter an integer:\n"))
    y=int(input("Please enter an integer:\n"))
    res=x-y
    print(f"{x}-{y}={res}")

elif choice==3:
    x=int(input("Please enter an integer:\n"))
    y=int(input("Please enter an integer:\n"))
    res=x*y
    print(f"{x}×{y}={res}")

elif choice==4:
    x=int(input("Please enter an integer:\n"))
    y=int(input("Please enter an integer:\n"))
    res=x/y
    print(f"{x}÷{y}={res}")