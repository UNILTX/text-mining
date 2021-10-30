def org_file():
    f = open('part3/SMSSpamCollection.txt')
    data = f.read()
    a = f.('spam')
    b = ':'
    print(a + b)
    print(''.join([a, b]))
    return (''.join([a, b]))

print(org_file())


def ham_spam():
    f = open('part3/SMSSpamCollection.txt')
    data = f.read()
    sentence = data.splitlines()
    dic={}
    for i in range ("spam","ham"):
        list_sentence=[]
        for j in sentence:
            if j[0] == "spam":
                list_sentence.extend(j)
            if len(list_sentence)!=0:
                dic1={chr(i):list_sentence}
            dic.update(dic1)
            return dic
print(ham_spam())
