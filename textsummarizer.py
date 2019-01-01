"""
NOTES:
    
    - Add a bag of words classifer to indentify the subject of article
    
"""

#Import the Libraries
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from bs4 import BeautifulSoup
import requests
import re
import nltk

#Intro
default = 'https://medium.com/tksblog/to-my-younger-self-b82fbed56232'

whichSum = int(input("(1) Extractive (2) Abstractive"))
demo = int(input("(1) Demo (2) Enter your own URL"))

if demo == 1:
    url = default

if demo == 2:
    url = input("URL of article:")
    

"""EXTRACTIVE TEXT SUMMARIZER"""

if whichSum == 1:
    
    #Scrape the url for all paragraphs and create a collective string
    result = requests.get(url)
    c = result.content
    soup = BeautifulSoup(c)
    
    article_text = ''
    article = soup.findAll('p')
    for element in article:
        article_text += '\n' + ''.join(element.findAll(text = True))
    
    #Remove special characters, numbers, stopwords, etc. from the text
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
    article_text = re.sub(r'\s+', ' ', article_text)  
    
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)  
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)  
    
    
    words = word_tokenize(formatted_article_text) 
    stopWords = nltk.corpus.stopwords.words('english')
    
    #Tally word frequencies from the text
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    
    #Break text into sentences then assign values based on word frequencies
    sentences = sent_tokenize(article_text)
    sentenceValue = dict()
    
    for sentence in sentences:
    	for word, freq in freqTable.items():
    		if word in sentence.lower():
    			if sentence in sentenceValue:
    				sentenceValue[sentence] += freq
    			else:
    				sentenceValue[sentence] = freq
    
    
    sumValues = 0
    for sentence in sentenceValue:
    	sumValues += sentenceValue[sentence]
    
    # Average value of a sentence from original text
    average = int(sumValues / len(sentenceValue))
    
    #If a sentence's value exceeds the average * 1.2, include it in the summary
    summary = ''
    for sentence in sentences:
    	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
    		summary += " " + sentence
            
    #Print summary and analytics
    print("Original article URL: " + url + "\n")
    print(summary + "\n")
    print("Original word count: " + str(len(article_text.split())))
    print("Summarized word count: " + str(len(summary.split())))
    print("Percent reduction: " + str("%.2f" % (100 - len(summary.split()) * 100 / len(article_text.split()))) + "%")
    
"""ABSTRACTIVE TEXT SUMMARIZER"""

if whichSum == 2:
    print("Coming soon")
