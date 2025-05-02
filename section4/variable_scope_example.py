teacher ="Brian" # This is a global variable
number_of_cats = 3 # This is a global variable

def favorites():
    favorite_airplane = "PBY Catalina" # This is a local variable
    favorite_cat = "Squeaker" # This is a local variable
    
    print("Teacher's name:")
    print(teacher) # You can refer to a global variable inside any function
    
    print("Favorite airplane:")
    print(favorite_airplane)
    
    print("Number of cats:")
    print(number_of_cats) # You can refer to a global variable inside any function
    
print (teacher)
print (number_of_cats)
favorites()