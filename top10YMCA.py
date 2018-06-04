# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 11:17:28 2018

@author: Joel
"""

import collections
import pandas as pd
import matplotlib.pyplot as plt

# Read input file, note the encoding is specified here 
#Park Service Text Source: https://www.gutenberg.org/files/57246/57246-0.txt
inFile = open('ymcaSurveys642018.txt', encoding="utf8")
a = inFile.read()

# Stopwords
stopwords = set(line.strip() for line in open('stopwordsNLTK.txt'))

# Instantiate a dictionary, and for every word in the file, 
# Add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}

# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)

# Close the file
inFile.close()

# Create a data frame of the most common words 
# Draw a bar chart
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')