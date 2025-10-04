while True:
  print("_________________________________________________________")
  print("Welcome to Your ♥️  Mini Calci")
  print("Enter Your Choice from 1 to 6")
  print("1.Add  2.Sub  3.Mul  4.Div  5.Power 6.Exit")
  
  choice=int(input("Enter your choice : "))
  if(choice==6):
    print("Claci Close ❌")
    break
  if(choice not in [1,2,3,4,5]):
    print("❎  Invalid choice, Try from 1 to 6")
    continue
  
  a=float(input("Enter 1st Number: "))
  b=float(input("Enter 2nd number: "))
  
  print("_________________________________________________________")
  if(choice==1):
    print(f"{a}+{b} = ",a+b)
  elif(choice==2):
    print(f"{a}-{b} = ",a-b)
  elif(choice==3):
    print(f"{a} X {b} = ",a*b)
  elif(choice==4):
    if(b==0):
      print("Error, Cannot divided by Zero")
    else:
     print(f"{a} / {b} = ",a/b)
  elif(choice==5):
    print(f"{a} ^ {b} = ",a**b)
  else:
    print("Invalid choice, Try from 1 to 6")