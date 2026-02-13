# 3. Input a sentence and print words in separate lines.

# input a sentence from user
sentence = input("Enter a sentence: ")

# spilt sentence into words
words = sentence.split()

# display each words
for words in words:
    print(words)