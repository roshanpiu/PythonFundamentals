#boolean
#True and False are boolean not true and false

print(type(True))
print(type(False))

print(1==1)
print(1==2)
print(2>1)
print(1<1)

print("H" in "Hello World!")
print("H" in "abc")

if 6>5:
    print("Six is greater than 5")

if 0>2:
    print("Zero is greater than 2")
else:
    print("Zero is not greater than 2")

if "Roshan" in "Roshan Piumal":
    print("Your name found")


if 1>0 and "Hello" in "Hello World":
    print("both expressions are True")

if 0>1 and "Hello" or "Hello World":
    print("Only one or both conditions are ture")


sister = 15
brother = 12

if sister > brother:
    print("sister is older")
elif sister == brother:
    print("same age")
else:
    print("brother is older")
