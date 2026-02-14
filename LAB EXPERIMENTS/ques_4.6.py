#6.Program to count number of unique words in a given sentence using sets.

# input sentence from user
sentence = input("Enter a sentence: ")

# convert sentence into words
words = sentence.split()

'''we split a sentence using split(), we get a list of words.
But a list allows duplicates, while a set automatically removes duplicates.'''

unique_words = set(words)
count = len(unique_words)

# display result
print("Number of unique words are: ",count)