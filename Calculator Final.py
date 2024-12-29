want_loop=True
while want_loop:
 choice=int(input("Choose desired operator:\n Enter 1 for (+) Addition\n Enter 2 for (-) Subtraction\n Enter 3 for (×) Multiplication\n Enter 4 for (÷) Division\n"))
 if choice not in [1,2,3,4]:
  print("Invalid input;")
  input("Press enter to exit.")
 x=int(input("Please enter an integer:\n"))
 y=int(input("Please enter another integer:\n"))
 if choice==1:
    res=x+y
    print(f"{x}+{y}={res}")

 elif choice==2:
    res=x-y
    print(f"{x}-{y}={res}")

 elif choice==3:
    res=x*y
    print(f"{x}×{y}={res}")

 elif choice==4:
    if y==0:
     print("Division with 0 in Y value is not possible;")
    else:
     res=x/y
     print(f"{x}÷{y}={res}")
 want_loop=input("Run program again? (Y/N)\n")
 if want_loop=="n":
    print("Ending loop...\n")
    break
 if want_loop=="y":
     print("Repeating...\n")
 else:
    print("Invalid input;")
    break


input("Press enter to exit.")