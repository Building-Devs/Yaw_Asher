
n=int(input("Enter value"))
def assign3():
    
    # Outer loop for rows
    for i in range(1,n+1):
        
        # Inner loop for columns
        for j in range(1,2*n):
            
            # Conditions for creating the pattern
            if i+j==n+1 or j-i==n-1:
                print("*",end=" ")
            else:
                print(end="  ")
        print()

assign3()