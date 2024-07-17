#!/usr/bin/env python
# coding: utf-8

# In[1]:
#import required libraries

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq


# In[2]:
#define a function to generate a summary from a given text

def nltk_summarizer(raw_text):

    # Set of English stop words
    stopWords = set(stopwords.words("english"))

    # Dictionary to hold word frequencies
    word_frequencies = {}

    # Tokenize the text into words and compute word frequencies
    for word in nltk.word_tokenize(raw_text):  
        if word not in stopWords:  # Ignore stop words
            if word not in word_frequencies.keys():  # If word is not already in the dictionary
                word_frequencies[word] = 1  # Initialize frequency to 1
            else:
                word_frequencies[word] += 1  # Increment frequency

    # Find the maximum word frequency
    maximum_frequncy = max(word_frequencies.values())
    
    # Normalize word frequencies by dividing by the maximum frequency
    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)

    # Tokenize the text into sentences
    sentence_list = nltk.sent_tokenize(raw_text)
    
    # Dictionary to hold sentence scores
    sentence_scores = {}  
    
    # Compute sentence scores based on word frequencies
    for sent in sentence_list:  
        for word in nltk.word_tokenize(sent.lower()):  # Tokenize sentence into words
            if word in word_frequencies.keys():  # If word is in the frequency dictionary
                if len(sent.split(' ')) < 30:  # Consider only sentences with less than 30 words
                    if sent not in sentence_scores.keys():  # If sentence is not already in the dictionary
                        sentence_scores[sent] = word_frequencies[word]  # Initialize score with word frequency
                    else:
                        sentence_scores[sent] += word_frequencies[word]  # Increment score

    # Select the 7 highest-scoring sentences
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    # Join the selected sentences to form the summary
    summary = ' '.join(summary_sentences)  
    
    return summary  

