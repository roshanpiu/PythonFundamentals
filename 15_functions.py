def greeting(name):
    print("Hello "+ name)
    
greeting("Roshan")

def sum(numbers):
    total = 0;
    for number in numbers:
        total = total + number
    return total
    
number_list = [1,2,3,4,5]

total = sum(number_list)
print(total)

def start_with_vowel(string):
    return string[0] in "AEIOU"
    
print(start_with_vowel("Roshan"))
print(start_with_vowel("Ashan"))

names_list = ["Roshan","Irosha","Ramesh","Ashan"]

def filter_vowel_names(word_list):
    vowel_words = []
    for word in word_list:
        if start_with_vowel(word):      
            vowel_words.append(word)
    return vowel_words

print(filter_vowel_names(names_list))