import random
import string
from afinn import Afinn

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

def unique_words(hist):      
    num_unique = len(hist) 
    counts = hist.values() 
    return (num_unique, counts)



def main():
    hist = process_file('part3/Alittleprincess.txt', skip_header=True)
    # print(hist)
    print('Total number of words:', total_words(hist))
    
    t = most_common(hist, excluding_stopwords=True)
    print('The most common words are:')
    for freq, word in t[0:100]:
        print(word, '\t', freq)



if __name__ == '__main__':
    main()
