def assign1():
 user_input=int((input("Enter value")))

 for i in range(user_input):
   if (i==0): 
      print("","","","","","*")
   elif (i==1):
      print("","","","","","*","*")
   elif (i==2):
      print("","","","*","*","*","")
   else:
    # for columns
    for j in range(i+1):
       print("","*", end="")
    print()
assign1()