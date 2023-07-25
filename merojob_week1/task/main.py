def calculation():
    num =  str(input("Enter the number:"))

    result = None
    if num == str(100):
        result = 50
    elif num == str(50):
        result = 100
    else:
        print("Invalid input") 
        return   
    print("Output is:",result)    
calculation()        
