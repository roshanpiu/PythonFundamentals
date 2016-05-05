#print() function append a newline to the end of the line
#line.strip() removes the newline from the line
#open() returns a file handle "r" option for specifiying open file for reading

f = open("file.txt", "r")

words = []

for line in f:
    line = line.strip()
    print(line)
    words.append(line)
    
    
f.close()
print(len(words))

for word in words:
    if word[0] == "H":
        print(word)

f = open("output_file.txt", "w")

while True:
    participant = raw_input("participant name >")
    
    if participant == "exit":
        break
        
    score = raw_input("score for " + participant + " >")
    f.write(participant+","+score+"\n")

f.close()

f = open("output_file.txt", "r")

participants = {}

for line in f:
    entry = line.strip().split(",")
    participant = entry[0]
    score = entry[1]
    participants[participant] = score
    
f.close()

print(participants)


    