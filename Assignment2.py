def assign2():
 user_input=int(input("Enter value"))

# for rows 
 for i in range(user_input):
   if (i==0): 
      print("*")
   else:
    # for columns
    for j in range(i+1):
       print("","*", end="")
    print()
assign2()