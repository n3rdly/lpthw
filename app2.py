
phrase = "Giraffe Acadamy"
print(phrase + " is cool")  # this is called concatination
print(phrase.lower()) # this will make everything in the phrase lowercase
print(phrase.upper()) # this will make everything in the phrase uppercase
print(phrase.isupper()) # this will check if the phrase is all uppercase 
print(phrase.islower()) # this will check if the phrase is all lowercase

phrase = "THIS IS YELLING"
print(phrase.isupper())

phrase = "this is whispering" 
print(phrase.islower())

print(phrase.upper().isupper()) # this will convert the phrase into all upper case and check the value

print(len(phrase)) # this will tell length of a string

print(phrase[0]) # print the position (in this case it will print the t)
print(phrase[2])
print(phrase[0])

print(phrase.index("i")) # check the phrase for the first time the value is found
print(phrase.index("whispering")) # returns 8 since the w starts at the 8th position
print(phrase.replace("whispering","talking normal")) # replace certain words or letters in a string
