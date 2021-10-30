
def total_spam():
    f = open('part3/SMSSpamCollection.txt')
    """This functiom returns to the total emails in the txt"""
    number_of_emails = 0
    for line in f:
        email=line.strip()
        number_of_emails += 1
    return number_of_emails
print(total_spam())

def total_words():
    """This functiom returns to the total words in the txt"""
    f = open('part3/SMSSpamCollection.txt')
    data = f.read()
    words = data.split()
# print(words)
    return len(words)
print(total_words())

def total_spam():
     """This functiom returns to the total spam in the txt"""
     f = open('part3/SMSSpamCollection.txt')
     data = f.read()
     words = data.split()
     spam = words.count("spam")
     return spam
print(total_spam())


def total_ham():
     """This functiom returns to the total ham in the txt"""
     f = open('part3/SMSSpamCollection.txt')
     data = f.read()
     words = data.split()
     ham = words.count("ham")
     return ham
print(total_ham())


def 