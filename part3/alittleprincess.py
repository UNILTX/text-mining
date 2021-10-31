import string
import codecs
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
import matplotlib.pyplot as plt

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file."""
    hist = {}
    f = open(filename, encoding='UTF8')
    if skip_header:
        skip_gutenberg_header(f)
    
    strippables = string.punctuation + string.whitespace

    for line in f:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist

def skip_gutenberg_header(f):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in f:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency."""
    t=[]
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t


def least_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in acsending order of frequency."""
    t=[]
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    return t

def unique_words(hist):      
    num_unique = len(hist) 
    counts = hist.values() 
    return (num_unique, counts)


def sentence_token_nltk(str):
    # code refernce: https://zhuanlan.zhihu.com/p/41804488
    sent_tokenize_list = sent_tokenize(str)
    return sent_tokenize_list

def sentiment_score(sen):
    sen=str(sen)
    score = SentimentIntensityAnalyzer().polarity_scores(sen)
    return score 

def plotgraph():
    #  make a bar graph based on sentiment score
    name_list=['negative','neutural','positive','compound']
    num_list = [0.068,0.83,0.103,1.0]
    plt.bar(range(len(num_list)),num_list,tick_label=name_list)
    plt.show()
    return plt.show()

def main():

    hist = process_file('part3/Alittleprincess.txt', skip_header=True)
    # print(hist)
    print('Total number of words for the book The little princess :', total_words(hist))
    
    t = most_common(hist, excluding_stopwords=True)
    print('The most common words for the book The little princess are:')
    for freq, word in t[0:30]:
        print(word, '\t', freq)

    t = least_common(hist, excluding_stopwords=True)
    print('The least common words for the book The little princess are:')
    for freq, word in t[0:30]:
        print(word, '\t', freq)

    with codecs.open('part3/Alittleprincess.txt', 'r', encoding='utf-8') as fp:
        str = fp.read().strip()
    sentence_str = sentence_token_nltk(str)
    # print(sentence_str)

    t=sentiment_score(sentence_token_nltk(str))
    print('sentiment score for the book The little princess is:', t)

    plotgraph() 


if __name__ == '__main__':
    main()