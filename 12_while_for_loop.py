for i in [0,1,2,3,4]:
    print("Hello "+str(i))
    
countter = 0
while countter < 5:
    print("Hello " + str(countter))
    countter += 1
    
countter = 0
while True:
    print("Hello " + str(countter))
    countter += 1
    
    if countter >=5:
        break
        
print("Hello Human")

while True:
    user_input = input("> ")
    if user_input == "quit":   
        print("Goodbye human")
        break
    else:
        print(user_input)