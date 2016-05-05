my_names = ["Chanaka", "Roshan", "Ashan", "Hasith"]

for name in my_names:
    print("Hello " + name)
    
for name in my_names:
    if name[0] in "AEIOU":
        print(name + "starts with a vowel" )    
        
    
vowel_names = []        
for name in my_names:
    if name[0] in "AEIOU":
        vowel_names.append(name)

print(vowel_names)

prices = [102.89, 22.34, 44.32, 323.34, 55.22]

total = 0
for price in prices:
    total += price
    
print("Total = " +str(total))
print("Total = " + str(sum(prices)))