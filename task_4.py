#Reverse a string(without using [::-1] or built-in methods)

word = str(input("Enter a word: "))
reversed_word = ""

for letter in word:
    reversed_word = letter + reversed_word

print(reversed_word)