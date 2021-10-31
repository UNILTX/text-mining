from thefuzz import fuzz
import matplotlib.pyplot as plt
import numpy as np 
# NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data.


def total_spam(f):
    f = open('part3/SMSSpamCollection.txt')
    """This functiom returns to the total emails in the txt"""
    number_of_emails = 0
    for line in f:
        email=line.strip()
        number_of_emails += 1
    return number_of_emails
print(total_spam())

def total_words(f):
    """This functiom returns to the total words in the txt"""
    f = open('part3/SMSSpamCollection.txt')
    data = f.read()
    words = data.split()
# print(words)
    return len(words)
print(total_words())

def total_spam(f):
     """This functiom returns to the total spam in the txt"""
     f = open('part3/SMSSpamCollection.txt')
     data = f.read()
     words = data.split()
     spam = words.count("spam")
     return spam
print(total_spam())


def total_ham(f):
     """This functiom returns to the total ham in the txt"""
     f = open('part3/SMSSpamCollection.txt')
     data = f.read()
     words = data.split()
     ham = words.count("ham")
     return ham
print(total_ham())


def ham_spam(f):
    f = open('part3/SMSSpamCollection.txt')
    data = {}
    for line in f.readlines():
        k,v = line.strip().split('\t')
        if k not in data:
            data[k] = []
            data[k].append(v)
        else:
            data[k].append(v)
    return data
# print(ham_spam())

def text_similarity():
    a=" ".join(ham_spam()['spam'])
    b=" ".join(ham_spam()['ham'])
    c=fuzz.ratio(a, b)
    return c

print(text_similarity())

