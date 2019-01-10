"""

DATABASE BUILDER

"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from bs4 import BeautifulSoup
import requests
import re
import nltk
import csv

nltk.download('punkt')
nltk.download('stopwords')

reset = int(input("Would you like to delete all articles in the database? (0) No (1) Yes"))

if reset == 1:
    dictlist = []
    dictlist2 = []
    dictlist3 = []
    temp = []
    temp2 = []
    temp3 = []
    totalArticles = 0

if reset == 0:
    numArticles = int(input("How many articles are you entering?"))
    subject = input("What subject are these articles: Science, Technology or Life?").upper()
    
    if subject == "SCIENCE":
        for i in range (numArticles):
            
            #Scrape the url for all paragraphs and create a collective string
            url = input("URL of Article:")
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
    
    #If a sentence's value exceeds the average * 1.2, include it in the science_summary
            science_summary = ''
            for sentence in sentences:
                if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                    science_summary += " " + sentence
        

            temp2 = [science_summary, "SCIENCE"]
            dictlist2.append(temp2)
            
    
    if subject == "TECHNOLOGY":
        for i in range (numArticles):
            
            #Scrape the url for all paragraphs and create a collective string
            url = input("URL of Article:")
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
    
    #If a sentence's value exceeds the average * 1.2, include it in the tech_summary
            tech_summary = ''
            for sentence in sentences:
                if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                    tech_summary += " " + sentence
        

            temp = [tech_summary, "TECHNOLOGY"]
            dictlist.append(temp)
            
    if subject == "LIFE":
        for i in range (numArticles):
            
            #Scrape the url for all paragraphs and create a collective string
            url = input("URL of Article:")
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
    
    #If a sentence's value exceeds the average * 1.2, include it in the life_summary
            life_summary = ''
            for sentence in sentences:
                if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                    life_summary += " " + sentence
        

            temp3 = [life_summary, "LIFE"]
            dictlist3.append(temp3)

completeList = dictlist + dictlist2 + dictlist3

with open("subject_freq.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Article", "Subject"])
    writer.writerows(completeList)